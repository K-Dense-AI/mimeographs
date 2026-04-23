# mimeographs

> _mimeograph_ — a stencil duplicator; a machine for reproducing the same piece of writing, over and over, in anyone's hands.

A collection of **80 ready-to-use "expert" skills** — `SKILL.md` + `AGENTS.md` files that clone the thinking of a specific person (a founder, a scientist, a philosopher, an AI researcher) into your coding agent. Drop one into your project and the agent starts reasoning the way that person does: the frameworks they reach for, the trade-offs they weigh, the anti-patterns they push back on.

Each folder under `mimeographs/` is one person. Pick the ones relevant to what you're building and install them.

> Every mimeograph in this repo was generated with [K-Dense-AI/mimeo](https://github.com/K-Dense-AI/mimeo). Mimeo reads the internet on your behalf — talks, essays, interviews, papers, letters — distills each source with a frontier model, clusters recurring ideas across dozens of sources, and emits the `SKILL.md` + `AGENTS.md` you see here. If you want to add a new expert, run mimeo yourself and open a PR.

---

## Who's in here

**Founders & operators** — Steve Jobs, Elon Musk, Bill Gates, Mark Zuckerberg, Warren Buffett, Andrew Carnegie, John D. Rockefeller, Henry Ford, Thomas Edison, Walt Disney, Oprah Winfrey, Sara Blakely, Whitney Wolfe Herd, Anne Wojcicki, Judy Faulkner, Kiran Mazumdar-Shaw, Diane Hendricks, Marian Ilitch, Lynda Resnick, Thai Lee.

**Philosophers** — Aristotle, Plato, Socrates, Confucius, Descartes, Hume, Kant, Nietzsche, Wittgenstein, Heidegger, Hannah Arendt, Simone de Beauvoir, Iris Murdoch, Mary Midgley, Elizabeth Anscombe, Judith Butler, Mary Wollstonecraft, Martha Nussbaum, Hildegard of Bingen, Hypatia of Alexandria.

**AI & ML researchers** — Geoffrey Hinton, Yann LeCun, Yoshua Bengio, Jürgen Schmidhuber, Judea Pearl, Stuart Russell, Richard S. Sutton, Andrew Ng, Fei-Fei Li, Daphne Koller, Sebastian Thrun, Demis Hassabis, David Silver, Pieter Abbeel, Ilya Sutskever, Andrej Karpathy, Ian Goodfellow, Jeff Dean, Kaiming He, Christopher Manning.

**Scientists & researchers** — Aviv Regev, Eric S. Lander, Robert Langer, Shizuo Akira, Stacey Gabriel, Virginia M.-Y. Lee, Zhenan Bao, Zhong Lin Wang, and a cohort of leading epidemiologists (Walter C. Willett, Frank B. Hu, Graham A. Colditz, JoAnn E. Manson, Julie E. Buring, Kay-Tee Khaw, Meir J. Stampfer, Ronald C. Kessler, Tamara B. Harris, Terrie E. Moffitt, Dorret I. Boomsma, Albert Hofman).

Run `ls mimeographs/` for the full list.

---

## Two flavors of the same person

Each folder contains both formats, so you can pick whichever fits your workflow:

```
mimeographs/steve-jobs/
├── SKILL.md           # on-demand: agent loads it when the task matches its description
├── AGENTS.md          # always-on: agent reads it every time it works in this directory
└── references/
    ├── principles.md
    ├── frameworks.md
    ├── mental-models.md
    ├── quotes.md
    └── sources.md
```

### `SKILL.md` — on-demand expertise

A `SKILL.md` is a self-describing capability that the agent loads **only when it's relevant to the task**. It has YAML frontmatter with a `name` and a `description`; the agent reads that description and decides whether to pull the skill in.

Use this when you want a library of experts that get invoked situationally — e.g. the Jobs skill fires when you're designing a product, the Buffett skill fires when you're evaluating a business, the Wittgenstein skill fires when you're untangling a definitional mess.

### `AGENTS.md` — always-on defaults

An `AGENTS.md` is a single markdown file the agent reads at the start of **every** session in that directory. No frontmatter, no triggering — it's always active.

Use this when you want an expert's defaults baked into the agent's everyday behavior in a specific project. Drop `mimeographs/steve-jobs/AGENTS.md` into a product repo and every code review, every design decision, every PR description will be filtered through Jobs's stance on craftsmanship and user experience.

You generally want **one `AGENTS.md` per project** and **many `SKILL.md`s in your global library**.

---

## Installation

### Option 1: `npx skills add` (recommended, all platforms)

Install one or more experts with a single command. Works with **Claude Code**, **Cursor**, **Codex**, **Gemini CLI**, and any other agent that supports the open Agent Skills standard:

```bash
# Install a single mimeograph
npx skills add K-Dense-AI/mimeographs/steve-jobs

# Install several at once
npx skills add K-Dense-AI/mimeographs/steve-jobs K-Dense-AI/mimeographs/warren-buffett

# Install the whole collection (60 experts)
npx skills add K-Dense-AI/mimeographs
```

`npx skills add` figures out the right install location for your agent (for example, `~/.claude/skills/` for Claude Code, `.cursor/skills/` for Cursor) and places the files there.

> Replace `K-Dense-AI/mimeographs` with the matching `owner/repo` slug if you've forked this repo.

### Option 2: GitHub CLI (`gh skill`)

If you have the GitHub CLI v2.90.0+:

```bash
# Install one
gh skill install K-Dense-AI/mimeographs steve-jobs

# Target a specific agent host
gh skill install K-Dense-AI/mimeographs steve-jobs --agent claude-code
gh skill install K-Dense-AI/mimeographs steve-jobs --agent cursor
gh skill install K-Dense-AI/mimeographs steve-jobs --agent codex
gh skill install K-Dense-AI/mimeographs steve-jobs --agent gemini

# Pin to a release tag or commit SHA
gh skill install K-Dense-AI/mimeographs steve-jobs --pin v0.1.0
```

### Option 3: Manual copy

Every mimeograph is just plain markdown. You can copy the folder anywhere your agent looks for skills:

```bash
# Claude Code (user-level)
cp -r mimeographs/steve-jobs ~/.claude/skills/

# Claude Code (project-level)
cp -r mimeographs/steve-jobs .claude/skills/

# Cursor (project-level)
cp -r mimeographs/steve-jobs .cursor/skills/

# Or just drop an AGENTS.md at the root of your repo
cp mimeographs/steve-jobs/AGENTS.md ./AGENTS.md
```

Restart your agent after installing so it picks up the new files.

---

## Using a `SKILL.md`

Once installed, skills auto-trigger whenever the agent decides the description matches the task. You don't have to do anything — just describe the problem you're working on, and the agent will pull in the right expert on its own.

If you want to invoke one explicitly, most platforms (Claude Code, Cursor, Codex, Gemini CLI, Copilot CLI) support slash-command style invocation — e.g. `/skill steve-jobs` — or you can just mention the skill by name in plain English ("use the steve-jobs skill"). Check your agent's docs for the exact syntax.

Natural-language examples that will auto-trigger the relevant skill:

```
"I'm designing the onboarding flow for a new consumer iOS app. Help me think through it."
→ triggers steve-jobs

"Should we acquire this SaaS company trading at 14x ARR?"
→ triggers warren-buffett

"I can't tell if my definition of 'fairness' is actually coherent or just vibes."
→ triggers ludwig-wittgenstein

"Design a prospective cohort study for a dietary intervention."
→ triggers walter-c-willett

"I'm debugging a transformer training run that's diverging after 10k steps."
→ triggers andrej-karpathy
```

---

## Using an `AGENTS.md`

`AGENTS.md` is the simpler of the two. It's a plain markdown file with no frontmatter and no triggering logic — the agent reads it at the start of every session in the directory where it lives.

Most agents (Cursor, Codex CLI, Gemini CLI, GitHub Copilot CLI, Aider, and others) look for an `AGENTS.md` at the root of your project. Drop one in and you're done:

```bash
# Install Steve Jobs as the always-on default for this project
cp mimeographs/steve-jobs/AGENTS.md ./AGENTS.md
```

Now every time the agent works in this repo — writing code, reviewing PRs, proposing architectures — it starts from Jobs's default stance: user experience first, delete more than you add, no committees, no speeds-and-feeds thinking.

> Already have an `AGENTS.md` in your repo? You can either merge them by hand (recommended for short ones) or append the mimeograph as a section:
>
> ```bash
> echo -e "\n---\n" >> AGENTS.md
> cat mimeographs/steve-jobs/AGENTS.md >> AGENTS.md
> ```

### When to pick which

| You want...                                                     | Use           |
| --------------------------------------------------------------- | ------------- |
| A library of experts, each firing only when relevant            | `SKILL.md`    |
| One expert's defaults baked into everything in a given project  | `AGENTS.md`   |
| Both — a project default plus a broader on-demand library       | Both          |

You can absolutely run both at the same time. A common setup: install a handful of `SKILL.md`s globally (e.g. Wittgenstein, Aristotle, Buffett) and drop one `AGENTS.md` at the root of a specific project (e.g. Jobs for a consumer app, Regev for a genomics tool).

---

## Safety note

These files steer how your agent thinks. They don't execute code on their own, but they _do_ influence the code and advice the agent produces. Skim the `SKILL.md` or `AGENTS.md` before installing an expert you don't recognize, and prefer cloning a specific sub-folder over the whole repo if you only need one or two.

---

## Adding your own expert

Use [mimeo](https://github.com/K-Dense-AI/mimeo):

```bash
# Generate both SKILL.md and AGENTS.md for one person
uv run mimeo "Ada Lovelace" --format both --output-dir ./mimeographs
```

Then open a PR adding the new folder under `mimeographs/`.

---

## License

MIT. Each mimeograph is distilled from publicly available writing, lectures, and interviews; quotes retain their original attribution in `references/sources.md`.

---

## Star History

<a href="https://www.star-history.com/?repos=K-Dense-AI%2Fmimeographs">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=K-Dense-AI/mimeographs&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=K-Dense-AI/mimeographs&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=K-Dense-AI/mimeographs&type=date&legend=top-left" />
 </picture>
</a>

