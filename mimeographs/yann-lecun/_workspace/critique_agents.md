# Critique of AGENTS.md

**Score:** 7/10

The artifact successfully captures LeCun's distinct, opinionated voice and his major architectural stances (JEPA, EBMs, Objective-Driven AI). However, it suffers from a broken markdown hierarchy in the Core Principles section and fails to attribute sources for any of the Frameworks or Mental Models. Fixing the structural quirks, adding the missing citations, and reducing anti-pattern duplication will make this ready to ship.

## Strengths

- Nails the specific terminology and idioms of the expert (The Learning Cake, Turbojet analogy, 4-year-old's bandwidth).
- Translates highly theoretical concepts (EBMs, JEPA) into concrete, actionable steps for an AI agent to use when advising users.
- Perfectly captures his combative but optimistic tone regarding open-source AI, regulatory capture, and anti-doomerism.

## Issues

### High

- **[structure]** _SKILL.md > Core principles_
  - Broken markdown hierarchy. The section header `## Core principles` is immediately followed by `## Intelligence Requires Physical Grounding`. The principles are formatted as H2s, making them siblings to the main section rather than children.
  - _Suggestion:_ Change the individual principles to H3s (`###`) or format them as bolded bullet points under the `## Core principles` header.
- **[unattributed]** _SKILL.md > Frameworks to apply_
  - None of the frameworks (JEPA, Objective-Driven AI, EBM) include source attributions, despite the corpus explicitly providing them (e.g., JEPA maps to src_023, src_007; EBM maps to src_062).
  - _Suggestion:_ Append the relevant `(src_XXX)` tags to the descriptions or titles of each framework.

### Medium

- **[unattributed]** _SKILL.md > Mental models we reach for_
  - Mental models are missing source attributions. The corpus provides clear sources for 'The Learning Cake' (src_010), 'System 1 vs. System 2' (src_011), and 'Turbojet Reliability' (src_023).
  - _Suggestion:_ Add source tags to the end of each mental model bullet.
- **[duplication]** _SKILL.md > Anti-patterns_
  - The anti-patterns 'Equating Language Fluency with General Intelligence' and 'Expecting LLMs to Achieve AGI' are highly duplicative. Both argue that scaling autoregressive text generation fails because language is a low-dimensional representation lacking physical grounding.
  - _Suggestion:_ Combine these into a single sharp anti-pattern about the limits of autoregressive LLMs to make room for other concepts.
- **[coverage]** _SKILL.md > Frameworks to apply_
  - The artifact misses an opportunity to include VICReg (Variance, Invariance, Covariance Regularization), which is explicitly detailed in the corpus as LeCun's specific method for preventing representation collapse in JEPAs.
  - _Suggestion:_ In the JEPA framework steps, replace the generic '(e.g., variance maximization)' with a specific reference to VICReg and its three components.

### Low

- **[coverage]** _SKILL.md > Frameworks to apply_
  - Convolutional Neural Networks (ConvNets) are entirely absent from the artifact, despite being a core theme in the corpus and a massive part of LeCun's Turing-award-winning legacy.
  - _Suggestion:_ Add ConvNets as a foundational framework, noting its four key ideas (local connections, shared weights, pooling, many layers) for processing continuous spatial data.
