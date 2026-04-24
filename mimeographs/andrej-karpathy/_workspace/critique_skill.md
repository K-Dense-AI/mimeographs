# Critique of SKILL.md

**Score:** 6/10

The artifact successfully captures Karpathy's recent focus on LLMs, Software 3.0, and vibe coding, but completely erases his foundational work in autonomous driving, vision, and reinforcement learning. Additionally, the artifact suffers from severe concept duplication, repeating the same ideas about 'building from scratch' and 'keeping AI on a leash' across principles, heuristics, and anti-patterns. Consolidating these repetitions will make room for a more balanced representation of his expertise.

## Strengths

- Excellent capture of Karpathy's specific idioms, particularly 'Software 3.0', 'Vibe Coding', and 'Summoning Ghosts'.
- The 'Jagged Intelligence' and 'Anterograde Amnesia' mental models are perfectly surfaced and highly actionable for users building LLM apps.
- Good structural use of the reference files, with accurate source attributions and direct quotes backing up the frameworks.

## Issues

### High

- **[coverage]** _Entire Artifact_
  - Karpathy's extensive work and mental models regarding Autonomous Driving, Vision, and End-to-End Optimization (e.g., 'The Data Engine', 'Meat vs Silicon Computer', 'Vision Alone') are completely missing. Given his tenure as Director of AI at Tesla, this is a massive gap in his expert profile.
  - _Suggestion:_ Add a section or principles covering his approach to physical AI and vision, specifically 'The Data Engine' loop, 'End-to-End Optimization', and the 'Meat vs Silicon Computer' mental model.

### Medium

- **[duplication]** _Core principles, Heuristics, Anti-patterns_
  - The concept of 'Building from scratch' is repeated three times: as a Core Principle ('Build from Scratch to Understand'), a Heuristic ('Build to Understand'), and an Anti-pattern ('Relying on Automated Tools Without Understanding').
  - _Suggestion:_ Keep it as a Core Principle and remove the redundant entries in Heuristics and Anti-patterns to make room for missing concepts.
- **[duplication]** _Core principles, Heuristics, Anti-patterns_
  - The concept of human oversight is highly redundant. 'Keep the AI on a Leash' (Principle), 'AI Generates, Human Verifies' (Heuristic), and 'Jumping to Full Autonomy' (Anti-pattern) all say the exact same thing with cosmetic rewording.
  - _Suggestion:_ Consolidate into a single strong principle or heuristic about 'Partial Autonomy / The Iron Man Suit' and remove the duplicates.
- **[coverage]** _references/mental-models.md_
  - The artifact misses Karpathy's critical insights on Reinforcement Learning, specifically 'RLHF is Gameable', 'RL Unlocks Emergent Reasoning', and 'Sucking Supervision Through a Straw'. These are core to his pedagogy on how LLMs actually learn to reason.
  - _Suggestion:_ Add his RL mental models to the references and integrate 'RL Unlocks Emergent Reasoning' into the main skill description when discussing LLM training.
- **[coverage]** _Core principles_
  - A major recent theme of Karpathy's—'Code is Ephemeral and Discardable'—is missing. This is a fundamental shift in his view of software engineering under Software 3.0.
  - _Suggestion:_ Add 'Code is Ephemeral' as a core principle or mental model, explaining that AI lowers the cost of code to zero, allowing for single-use, throwaway software.

### Low

- **[vagueness]** _Core principles > Agency Over Intelligence_
  - The phrasing 'ability to take action, set boundary conditions, and drive outcomes' is a bit generic. Karpathy's specific idiom here relates to the 'Human-to-Agent Ratio' and humans acting as the 'director of the token generating swarm'.
  - _Suggestion:_ Sharpen the principle by explicitly using his terminology: 'Humans must transition from writing code to acting as the director of a token-generating swarm, managing high human-to-agent ratios.'
