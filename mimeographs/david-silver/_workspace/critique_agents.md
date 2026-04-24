# Critique of AGENTS.md

**Score:** 6/10

The artifact captures David Silver's tabula rasa philosophy well, but it beats the 'human data is bad' drum so many times that it crowds out his actual technical expertise. It reads more like a philosophical manifesto than an actionable RL engineering guide, missing crucial mechanical insights about MCTS, policy gradients, and exploration. Furthermore, the frameworks section completely drops required source attributions.

## Strengths

- Strong, opinionated 'Default stance' that accurately reflects Silver's uncompromising pursuit of generality.
- Excellent extraction and application of Silver's specific mental models, particularly the 'Cake Recipe' and 'Oscilloscope' metaphors.
- The 'Rising Tide' framework is a fantastic inclusion for helping users scope AI projects realistically.

## Issues

### High

- **[unattributed]** _Frameworks to apply_
  - None of the frameworks include source attributions (e.g., `src_XXX`), despite the corpus providing clear sources for them (e.g., src_014, src_049 for AlphaZero; src_007, src_018 for Rising Tide; src_020 for RL Agent Decomposition).
  - _Suggestion:_ Append the relevant `(src_XXX)` tags to the end of each framework's description or steps.

### Medium

- **[duplication]** _Core principles_
  - The first three principles ('The Era of Experience Over Human Data', 'Tabula Rasa Learning Surpasses Human Expertise', and 'The Purity of Self-Learning') are the exact same concept repeated with cosmetic rewording: human data limits performance, throw it out so the system can learn for itself.
  - _Suggestion:_ Consolidate these into a single, punchy principle about discarding human data to break the performance ceiling. Use the freed-up space for technical principles.
- **[coverage]** _Core principles & Frameworks to apply_
  - The artifact undersurfaces Silver's deep technical RL expertise. The corpus contains rich details on MCTS as a policy improvement operator, Actor-Critic architectures, DQN, and the exploration vs. exploitation tradeoff, but the artifact ignores these in favor of high-level philosophy.
  - _Suggestion:_ Add a principle on 'MCTS as a Policy Improvement Operator' or 'Breaking the IID Assumption'. Include a framework for 'Actor-Critic' or 'DQN' to give the agent concrete technical scaffolding.
- **[duplication]** _Anti-patterns_
  - The first two anti-patterns ('Hardcoding Human Knowledge' and 'Relying Exclusively on Human Data') are just the first three Core Principles restated in the negative. This means the same idea is repeated five times in the document.
  - _Suggestion:_ Replace these with technical anti-patterns from the corpus, such as 'Using Monte-Carlo for Off-Policy Control' or 'Ignoring State Aliasing'.

### Low

- **[voice]** _Default stance > Unify under reward_
  - The phrasing 'Unify under reward' is a bit generic. The corpus specifically refers to this as 'The Reward Hypothesis'.
  - _Suggestion:_ Rename the bullet to 'Assume the Reward Hypothesis:' to ground it in Silver's specific academic terminology.
