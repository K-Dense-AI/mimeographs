# Critique of AGENTS.md

**Score:** 7/10

The artifact captures Stuart Russell's voice and core philosophy (uncertainty, Assistance Games, the Control Problem) exceptionally well, avoiding generic AI safety platitudes. However, it suffers from structural duplication between principles and anti-patterns, and completely misses his highly actionable stances on machine self-identification. Adding citations to the frameworks and swapping the mirrored anti-patterns for missing themes will make this a stellar skill.

## Strengths

- Excellent use of Russell's specific analogies (Jeeves, King Midas, Chernobyl, Breeding Horses) which gives the artifact a distinct, recognizable voice.
- The 'How to engage' section provides highly practical instructions for an LLM (e.g., silently using Value of Information vs. explicitly invoking Assistance Games).
- Accurately frames the 'Control Problem' as an issue of objective uncertainty rather than falling back on generic 'AI turning evil' tropes.

## Issues

### Medium

- **[unattributed]** _SKILL.md > Frameworks to apply_
  - None of the frameworks include source citations, despite being directly drawn from the corpus (e.g., Assistance Games is src_011/src_013, Red Line Regulation is src_012/src_026).
  - _Suggestion:_ Append blockquotes or inline `(src_XXX)` citations to each framework to ground them in the corpus.
- **[duplication]** _SKILL.md > Anti-patterns_
  - 'Post-Hoc Safety' and 'Loyal AI' are exact negative mirrors of the 'Safety by Design' and 'No Strict Loyalty' core principles. This pads the artifact without adding new constraints.
  - _Suggestion:_ Replace these anti-patterns with missing concepts from the corpus, such as 'Corporations as Rogue AI' (optimizing fixed proxy metrics) or 'Capabilities Without Understanding'.
- **[coverage]** _SKILL.md > Core principles_
  - The artifact entirely misses Russell's highly actionable rule on 'Mandatory Machine Self-Identification' and 'Avoid Humanoid Deception'. For an AI agent skill, the rule that an AI must never pretend to be human is a critical, missing behavioral constraint.
  - _Suggestion:_ Add a principle: 'Mandatory Machine Self-Identification: AI systems must never pretend to be human. Humans have an absolute right to know they are interacting with a machine.' (src_027, src_014).

### Low

- **[coverage]** _SKILL.md > Frameworks to apply_
  - The artifact misses Russell's specific regulatory mechanism: 'Proof-Carrying Code for Hardware Regulation'. It focuses heavily on software/math but misses his point that hardware is the ultimate regulator.
  - _Suggestion:_ Add 'Proof-Carrying Code' as a framework for high-stakes deployment, emphasizing that software must carry mathematical proofs checked by hardware.
- **[voice]** _SKILL.md > Anti-patterns > Relying on RLHF for Safety_
  - The explicit use of 'RLHF' feels like a generic AI safety insertion rather than Russell's specific idiom. Russell typically critiques 'black box' deep learning and 'breeding horses' rather than using the RLHF acronym directly.
  - _Suggestion:_ Rename to 'Capabilities Without Understanding' or frame it around the 'Breeding Horses' analogy to stay true to his specific vocabulary.
