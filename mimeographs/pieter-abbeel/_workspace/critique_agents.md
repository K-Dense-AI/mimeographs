# Critique of AGENTS.md

**Score:** 6/10

The artifact captures Abbeel's pragmatic, robotics-first voice well, but suffers from severe structural duplication, repeating the exact same concepts across principles, frameworks, and anti-patterns. It also completely misses key frameworks from the corpus like Hindsight Experience Replay and fails to attribute sources in the latter half of the document. While usable, it needs a structural pass to consolidate redundant ideas and surface missing technical depth.

## Strengths

- Strong, opinionated default stance that accurately reflects Abbeel's preference for data over rules and physical reality over simulation.
- Excellent translation of the 'Software 2.0' concept into actionable advice for steering users away from complex conditional logic.
- The 'How to engage' section provides highly specific, behavioral instructions on when to push back on users (e.g., deploying pure RL on physical hardware).

## Issues

### Medium

- **[duplication]** _Core principles, Frameworks, Anti-patterns_
  - Extreme repetition of 'Domain Randomization' and 'Bootstrapping Real-World RL'. Both concepts are listed as Core Principles, then repeated as step-by-step Frameworks, and then repeated again as Anti-patterns ('Perfecting the Simulator' and 'Deploying Pure RL from Scratch'). This wastes space and makes the skill feel thin.
  - _Suggestion:_ Consolidate. Keep 'Domain Randomization' and 'Bootstrapped RL' strictly as Frameworks. Replace their slots in Core Principles with unused principles from the corpus, such as 'Deep Learning as the Path to AGI' or 'AI as a Meta-Discipline'.
- **[coverage]** _Frameworks to apply_
  - The 'Hindsight Experience Replay' framework is completely missing. The corpus explicitly details this 4-step framework for sparse-reward environments, which is a highly actionable and specific RL technique that users would benefit from.
  - _Suggestion:_ Add 'Hindsight Experience Replay' to the Frameworks section, detailing the 4 steps provided in the corpus.
- **[unattributed]** _Frameworks to apply_
  - None of the frameworks include source attributions (e.g., src_023, src_027), despite the prompt requiring frameworks to point back to at least one src_XXX when supported by the corpus.
  - _Suggestion:_ Append the relevant source tags (e.g., (src_023, src_027) for Domain Randomization) to the end of each framework's description or steps.

### Low

- **[unattributed]** _Core principles > Bootstrapping Real-World RL_
  - This principle is missing a source attribution or representative quote, even though the corpus clearly links this concept to src_017.
  - _Suggestion:_ Add a citation to (src_017) at the end of the principle's description.
- **[coverage]** _Frameworks to apply_
  - The artifact mentions 'Adaptive Policies' as a principle but misses the opportunity to include the concrete 'Model-Based RL via Meta Policy Optimization (MB-MPO)' framework provided in the corpus.
  - _Suggestion:_ Convert the 'Adaptive Policies' principle into the MB-MPO framework to give the agent a concrete, step-by-step method for model-based RL.
