#!/usr/bin/env python3
"""Generate the browseable expert catalog from the mimeograph folders.

Reads every ``mimeographs/<slug>/SKILL.md`` and emits two artifacts that give
users a single front door to the collection instead of 80 separate files:

    INDEX.md      a category-grouped, Ctrl-F-able table of every expert
    catalog.json  the same data as structured records for tooling/agents

It also refreshes the counts line in README.md between the
``<!-- CATALOG:COUNTS START -->`` / ``<!-- CATALOG:COUNTS END -->`` markers,
if they are present.

Run ``python scripts/build_catalog.py`` to (re)generate, or
``python scripts/build_catalog.py --check`` in CI to fail when anything is
stale (e.g. a new expert was added with ``mimeo`` but the catalog wasn't
rebuilt, or an expert isn't assigned to a category).

No third-party dependencies — the frontmatter here is just ``name`` plus a
single-line ``description``, and the display name comes from the body H1.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

# The owner/repo slug used in install commands. Change this once if you fork.
REPO = "K-Dense-AI/mimeographs"

REPO_ROOT = Path(__file__).resolve().parent.parent
MIMEOGRAPHS_DIR = REPO_ROOT / "mimeographs"
INDEX_PATH = REPO_ROOT / "INDEX.md"
CATALOG_JSON_PATH = REPO_ROOT / "catalog.json"
README_PATH = REPO_ROOT / "README.md"

COUNTS_START = "<!-- CATALOG:COUNTS START -->"
COUNTS_END = "<!-- CATALOG:COUNTS END -->"

# Curated category -> ordered list of folder slugs. Categories and ordering
# mirror the README's "Who's in here" groupings. When you add an expert with
# mimeo, add its slug here too; `--check` fails loudly if a folder is missing.
CATEGORIES: "OrderedDict[str, list[str]]" = OrderedDict(
    [
        (
            "Founders & operators",
            [
                "steve-jobs", "elon-musk", "bill-gates", "mark-zuckerberg",
                "warren-buffett", "andrew-carnegie", "john-d-rockefeller",
                "henry-ford", "thomas-edison", "walt-disney", "oprah-winfrey",
                "sara-blakely", "whitney-wolfe-herd", "anne-wojcicki",
                "judy-faulkner", "kiran-mazumdar-shaw", "diane-hendricks",
                "marian-ilitch", "lynda-resnick", "thai-lee",
            ],
        ),
        (
            "Philosophers",
            [
                "aristotle", "plato", "socrates", "confucius", "rene-descartes",
                "david-hume", "immanuel-kant", "friedrich-nietzsche",
                "ludwig-wittgenstein", "martin-heidegger", "hannah-arendt",
                "simone-de-beauvoir", "iris-murdoch", "mary-midgley",
                "elizabeth-anscombe", "judith-butler", "mary-wollstonecraft",
                "martha-nussbaum", "hildegard-of-bingen", "hypatia-of-alexandria",
            ],
        ),
        (
            "AI & ML researchers",
            [
                "geoffrey-hinton", "yann-lecun", "yoshua-bengio",
                "jurgen-schmidhuber", "judea-pearl", "stuart-russell",
                "richard-s-sutton", "andrew-ng", "fei-fei-li", "daphne-koller",
                "sebastian-thrun", "demis-hassabis", "david-silver",
                "pieter-abbeel", "ilya-sutskever", "andrej-karpathy",
                "ian-goodfellow", "jeff-dean", "kaiming-he",
                "christopher-manning",
            ],
        ),
        (
            "Scientists & researchers",
            [
                "aviv-regev", "eric-s-lander", "robert-langer", "shizuo-akira",
                "stacey-gabriel", "virginia-m-y-lee", "zhenan-bao",
                "zhong-lin-wang", "walter-c-willett", "frank-b-hu",
                "graham-a-colditz", "joann-e-manson", "julie-e-buring",
                "kay-tee-khaw", "meir-j-stampfer", "ronald-c-kessler",
                "tamara-b-harris", "terrie-e-moffitt", "dorret-i-boomsma",
                "albert-hofman",
            ],
        ),
    ]
)

H1_RE = re.compile(r"^#\s+Thinking like\s+(.+?)\s*$", re.MULTILINE)


class CatalogError(Exception):
    """Raised when the source folders can't be turned into a valid catalog."""


def discover_slugs() -> "list[str]":
    """Return every folder under mimeographs/ that contains a SKILL.md."""
    return sorted(
        p.name
        for p in MIMEOGRAPHS_DIR.iterdir()
        if p.is_dir() and (p / "SKILL.md").is_file()
    )


def parse_frontmatter(text: str) -> "dict[str, str]":
    """Parse the leading ``---`` YAML block. Handles the simple key: value
    shape these skills use (single-line values only)."""
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    fields: "dict[str, str]" = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def display_name(slug: str, body: str) -> str:
    """Pull the display name from the body's '# Thinking like X' heading,
    falling back to a title-cased slug."""
    match = H1_RE.search(body)
    if match:
        return match.group(1)
    return slug.replace("-", " ").title()


def first_sentence(description: str) -> str:
    """The leading identity sentence — used as the compact 'focus' blurb."""
    # Split on the first period that is followed by a space + capital letter,
    # so abbreviations like "Apple Inc." or "Eric S. Lander" don't end it early.
    match = re.search(r"\.\s+(?=[A-Z])", description)
    return description[: match.start() + 1] if match else description


def category_of(slug: str) -> "str | None":
    for category, slugs in CATEGORIES.items():
        if slug in slugs:
            return category
    return None


def install_commands(slug: str) -> "dict[str, str]":
    return {
        "npx": f"npx skills add {REPO}/{slug}",
        "gh": f"gh skill install {REPO} {slug}",
        "manual": f"cp -r mimeographs/{slug} ~/.claude/skills/",
    }


def build_records() -> "list[dict]":
    """Read every expert folder into a structured record, in curated
    category order (uncategorized experts sorted at the end)."""
    slugs = discover_slugs()
    known = set(slugs)

    # Validate the category map against what's actually on disk.
    mapped = {s for slugs_ in CATEGORIES.values() for s in slugs_}
    stale = sorted(mapped - known)
    if stale:
        raise CatalogError(
            "CATEGORIES references folders that don't exist: "
            + ", ".join(stale)
        )
    uncategorized = sorted(known - mapped)
    if uncategorized:
        raise CatalogError(
            "These experts aren't assigned to a category in build_catalog.py "
            "(add them to CATEGORIES): " + ", ".join(uncategorized)
        )

    # Curated order: by category, then by the order within each category.
    ordered: "list[str]" = []
    for slugs_ in CATEGORIES.values():
        ordered.extend(s for s in slugs_ if s in known)

    records = []
    for slug in ordered:
        folder = MIMEOGRAPHS_DIR / slug
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        description = fm.get("description", "").strip()
        if not description:
            raise CatalogError(f"{slug}/SKILL.md has no description")
        body = text.split("---", 2)[-1]
        references = sorted(
            f"references/{p.name}"
            for p in (folder / "references").glob("*.md")
        ) if (folder / "references").is_dir() else []
        records.append(
            {
                "slug": slug,
                "name": display_name(slug, body),
                "category": category_of(slug),
                "description": description,
                "summary": first_sentence(description),
                "path": f"mimeographs/{slug}",
                "files": {
                    "skill": (folder / "SKILL.md").is_file(),
                    "agents": (folder / "AGENTS.md").is_file(),
                    "avatar": (folder / "avatar.png").is_file(),
                    "references": references,
                },
                "install": install_commands(slug),
            }
        )
    return records


def esc(cell: str) -> str:
    """Escape a value for use inside a Markdown table cell."""
    return cell.replace("|", "\\|").replace("\n", " ").strip()


def render_index(records: "list[dict]") -> str:
    total = len(records)
    by_cat: "OrderedDict[str, list[dict]]" = OrderedDict(
        (c, []) for c in CATEGORIES
    )
    for r in records:
        by_cat[r["category"]].append(r)

    lines = [
        "<!-- Generated by scripts/build_catalog.py — do not edit by hand. -->",
        "# Catalog",
        "",
        f"All **{total} experts**, grouped by domain. "
        "Use your browser's find (Ctrl/Cmd-F) to search by what you're working "
        "on — the trigger conditions in each row contain the relevant keywords "
        "(e.g. \"cohort study\", \"capital allocation\", \"transformer\").",
        "",
        "Install any expert with the command in its row, or grab the whole "
        f"collection with `npx skills add {REPO}`.",
        "",
        "## Contents",
        "",
    ]
    for category, items in by_cat.items():
        anchor = category.lower().replace(" & ", "--").replace(" ", "-")
        lines.append(f"- [{category}](#{anchor}) ({len(items)})")
    lines.append("")

    for category, items in by_cat.items():
        lines.append(f"## {category}")
        lines.append("")
        lines.append("| Expert | Reach for this when… | Install |")
        lines.append("| --- | --- | --- |")
        for r in items:
            name_cell = f"**[{esc(r['name'])}]({r['path']}/)**"
            install_cell = f"`{r['install']['npx']}`"
            lines.append(
                f"| {name_cell} | {esc(r['description'])} | {install_cell} |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_catalog_json(records: "list[dict]") -> str:
    payload = {
        "repo": REPO,
        "count": len(records),
        "categories": list(CATEGORIES.keys()),
        "experts": records,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def render_counts_block(records: "list[dict]") -> str:
    counts = OrderedDict((c, 0) for c in CATEGORIES)
    for r in records:
        counts[r["category"]] += 1
    parts = " · ".join(f"{n} {c}" for c, n in counts.items())
    return f"**{len(records)} experts** — {parts}."


def update_readme_counts(records: "list[dict]") -> "str | None":
    """Return the README text with the counts block refreshed, or None if the
    markers aren't present (so this stays an opt-in, no-surprise edit)."""
    if not README_PATH.is_file():
        return None
    text = README_PATH.read_text(encoding="utf-8")
    if COUNTS_START not in text or COUNTS_END not in text:
        return None
    block = f"{COUNTS_START}\n{render_counts_block(records)}\n{COUNTS_END}"
    pattern = re.compile(
        re.escape(COUNTS_START) + r".*?" + re.escape(COUNTS_END), re.DOTALL
    )
    return pattern.sub(block, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail (exit 1) if any generated file is out of date, instead of "
        "writing. Use this in CI.",
    )
    args = parser.parse_args()

    try:
        records = build_records()
    except CatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    index_text = render_index(records)
    catalog_text = render_catalog_json(records)
    readme_text = update_readme_counts(records)

    targets = [
        (INDEX_PATH, index_text),
        (CATALOG_JSON_PATH, catalog_text),
    ]
    if readme_text is not None:
        targets.append((README_PATH, readme_text))

    if args.check:
        stale = []
        for path, want in targets:
            have = path.read_text(encoding="utf-8") if path.is_file() else None
            if have != want:
                stale.append(path.relative_to(REPO_ROOT))
        if stale:
            print(
                "error: catalog is out of date. Run "
                "`python scripts/build_catalog.py` and commit:\n  "
                + "\n  ".join(str(p) for p in stale),
                file=sys.stderr,
            )
            return 1
        print(f"ok: catalog up to date ({len(records)} experts)")
        return 0

    for path, want in targets:
        path.write_text(want, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO_ROOT)}")
    print(f"done: {len(records)} experts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
