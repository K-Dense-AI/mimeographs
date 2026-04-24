# Critique of AGENTS.md

**Score:** 7/10

The artifact captures Hassabis's rigorous, scientific voice exceptionally well, avoiding generic AI hype in favor of 'engineering science.' However, it completely misses his foundational methodology of using games as microcosms for AI development, which is heavily featured in the corpus. Additionally, it fails to attribute sources in the Frameworks and Mental Models sections, and suffers from some structural duplication.

## Strengths

- Nails the 'engineering science' and 'root node' terminology, perfectly capturing his academic rigor and ambition.
- Excellent translation of 'AI Hallucination as Hippocampal Amnesia' into a practical, unique mental model.
- Strong, opinionated 'Out-of-bounds' instruction that prevents the agent from applying Hassabis's heavy scientific frameworks to trivial CRUD apps.

## Issues

### High

- **[coverage]** _Entire artifact_
  - The artifact completely omits the 'Games as a Proving Ground / Microcosm' theme. Hassabis famously uses games (Atari, Go, StarCraft) because they provide clear objective functions, easy data generation, and safe simulation environments. This is a massive part of his methodology that is missing.
  - _Suggestion:_ Add a principle or framework around 'Games as the Ideal Microcosm' to guide users on how to set up safe, measurable, scaled-down simulation environments before tackling real-world problems.

### Medium

- **[unattributed]** _Frameworks to apply & Mental models we reach for_
  - None of the frameworks or mental models include source citations, despite the corpus explicitly providing them (e.g., 'Criteria for a Suitable AI Problem' maps to src_012, src_038; 'Root Node Problems' maps to src_016, src_019).
  - _Suggestion:_ Append the relevant (src_XXX) tags to the descriptions or titles of each framework and mental model.
- **[duplication]** _Default stance vs. Frameworks to apply_
  - The 'Default stance' bullets ('Notice search spaces first', 'Demand clear objective functions', 'Prioritize simulation') are almost word-for-word identical to the three steps in the 'Criteria for a Suitable AI Problem' framework.
  - _Suggestion:_ Keep the 'Default stance' focused on high-level worldview (e.g., treating AI as an engineering science, looking to neuroscience for inspiration) and reserve the specific 3-step checklist for the Framework section.
- **[coverage]** _Mental models we reach for_
  - The artifact misses the '10x Industrial Revolution' mental model. This is a highly specific, signature Hassabis framing for AGI's impact and speed, which is much more unique to him than 'Capability Overhang' (a broader AI industry term).
  - _Suggestion:_ Replace or augment 'Capability Overhang' with '10x Industrial Revolution' (AGI unfolding at 10 times the impact of the industrial revolution at 10 times the speed).

### Low

- **[vagueness]** _Core principles > Compute for Algorithmic Experimentation_
  - The 'In practice' advice ('Advise the user to test novel algorithmic approaches at a reasonable scale') is generic and misses the specific heuristic Hassabis uses for scaling.
  - _Suggestion:_ Incorporate his specific heuristic from the corpus: 'Scaling is an Artform'—advise adjusting the recipe at each scale and jumping by a maximum of one order of magnitude at a time.
