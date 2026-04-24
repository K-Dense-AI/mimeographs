# Critique of AGENTS.md

**Score:** 6/10

The artifact captures Kaiming He's structural approach to deep learning well, but suffers from severe duplication, repeating the exact same concepts (Residuals, Conditional Distributions) across Principles, Frameworks, Mental Models, and Anti-patterns. It also entirely misses the 'Mean Flows Algorithm' framework, leaving a major gap in his recent generative modeling work. On the positive side, it effectively translates highly technical concepts like OPQ and He Initialization into actionable agent behaviors.

## Strengths

- Accurately captures the structural, math-grounded voice of Kaiming He without resorting to generic motivational fluff.
- Effectively translates highly technical concepts (OPQ, He Initialization) into concrete, actionable agent behaviors.
- Maintains a strong, consistent focus on optimization and trainability rather than just scaling parameters.

## Issues

### High

- **[coverage]** _Frameworks to apply_
  - The 'Mean Flows Algorithm' framework is completely missing from the artifact, despite being a major, highly specific framework in the corpus detailing how to train one-step generative models using average velocity.
  - _Suggestion:_ Add the 'Mean Flows Algorithm' to the Frameworks section, detailing the steps for using average velocity and conditional flow matching for one-step generation.

### Medium

- **[duplication]** _Throughout (Principles, Frameworks, Mental Models, Anti-patterns)_
  - The 'Residual Learning' concept is heavily duplicated. It appears as a Core Principle, a Framework, a Mental Model, and an Anti-pattern, with almost identical descriptions (reformulate layers to learn a delta).
  - _Suggestion:_ Consolidate. Keep Residual Learning as a Core Principle and Framework, but remove it from Mental Models and Anti-patterns to make room for undersurfaced concepts like 'Integral vs. Finite Sum Reality'.
- **[duplication]** _Throughout (Principles, Frameworks, Anti-patterns)_
  - The concept of framing problems as conditional distributions is repeated across Core Principles ('Generative Models as Universal Solvers'), Frameworks ('Conditional Distribution Formulation'), and Anti-patterns ('Closed-Vocabulary Classification').
  - _Suggestion:_ Keep the Framework and the Anti-pattern, but replace the Core Principle with 'Generative Modeling as Distribution Mapping' to highlight the fundamental difference between generative and discriminative modeling.

### Low

- **[structure]** _Signature quotes_
  - The Signature Quotes section repeats quotes that were already used inline within the Core Principles section (e.g., src_042 and src_027).
  - _Suggestion:_ Use unique quotes in the Signature Quotes section, or remove the section entirely if all valuable quotes are already contextualized within the principles.
- **[vagueness]** _Default stance_
  - The bullet 'Notice structural bottlenecks first...' is slightly generic and reads like standard AI advice rather than Kaiming He's specific idiom.
  - _Suggestion:_ Sharpen to: 'Diagnose optimization degradation before adding parameters; if a deep network is hard to train, the architecture is structurally flawed, not just under-parameterized.'
