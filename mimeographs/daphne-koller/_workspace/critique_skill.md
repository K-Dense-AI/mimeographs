# Critique of SKILL.md

**Score:** 7/10

The artifact successfully captures Koller's pragmatic, interdisciplinary approach to AI in the physical sciences, nailing her specific idiom ('bits meet atoms', 'anti-hypothesis driven'). However, it suffers from structural fragmentation by burying her most powerful business and scientific models in reference files while surfacing generic career advice in the main prompt. Additionally, her core thesis on data generation is repeated redundantly across almost every category rather than being consolidated.

## Strengths

- Nails her specific terminology, especially 'bits meet atoms', 'anti-hypothesis driven', and 'bilingual professionals'.
- Accurately captures her pragmatic stance on AI as an amplifier of rigorous science rather than a magic wand.
- The anti-patterns section is exceptionally strong, particularly the warning against 'seductive plausibility' and hallucinated synthetic data.

## Issues

### Medium

- **[coverage]** _Main Skill File > Applying the frameworks_
  - The main skill file highlights 'Decision-Making for Maximum Impact' (a generic career framework) but completely omits her highly specific, high-leverage frameworks for drug discovery like 'The Inverted Funnel of Drug Development' or 'Drug Discovery as a Forked Road'.
  - _Suggestion:_ Replace the generic career framework in the main file with 'The Inverted Funnel of Drug Development' to better equip the agent for advising on AI/biotech business strategy.
- **[duplication]** _Across all files (Principles, Heuristics, Anti-patterns)_
  - The concept of 'Fit-for-purpose data' / 'Data is not fungible' is repeated cosmetically across Core Principles, Heuristics, Anti-patterns, and Mental Models. This wastes token space and dilutes the impact of the idea.
  - _Suggestion:_ Consolidate the data generation thesis into a single, powerful 'Data Printing Factory' principle or mental model, and remove the redundant entries in heuristics and anti-patterns.
- **[duplication]** _references/anti-patterns.md_
  - 'Siloed Disciplines / Throwing data over the wall' and 'Siloing disciplines' are listed as two separate anti-patterns with nearly identical descriptions.
  - _Suggestion:_ Merge these two anti-patterns into a single entry.

### Low

- **[structure]** _Main Skill File > How Daphne Koller reasons_
  - The text states 'For the rest of her mental models, see references/mental-models.md', but there is no actual 'Mental Models' section in the main file—they are just woven into the prose.
  - _Suggestion:_ Create a dedicated 'Mental Models' section in the main file to explicitly list 'Bilingual Professionals' and 'Bits Meet Atoms' before pointing to the reference file.
- **[vagueness]** _Main Skill File > Decision-Making for Maximum Impact_
  - The steps for this framework are phrased like generic self-help ('Identify a deep internal urgency to do something meaningful'). It lacks Koller's specific, pragmatic edge.
  - _Suggestion:_ Rewrite to focus strictly on her concept of 'disproportionate leverage'—evaluating where your specific background provides an outsized advantage compared to the next best person.
