# Critique of AGENTS.md

**Score:** 8/10

The artifact is a strong, highly specific representation of Judea Pearl's technical philosophy, but it leaves some of his most interesting AI-specific insights on the cutting room floor. Specifically, it misses his computational translations of human psychology (free will and empathy as AI design protocols) and duplicates a few core concepts across sections. However, the voice is exceptionally accurate, successfully avoiding generic statistics advice in favor of Pearl's rigorous, model-first worldview.

## Strengths

- Excellent use of Pearl's specific idioms (Babylonian vs. Greek science, the Demarcation Line, M-graphs) rather than generic data science terminology.
- The 'How to engage' section provides highly actionable, concrete triggers for when the AI should halt a conversation and demand a causal graph.
- Signature quotes are perfectly selected and directly support the behavioral instructions.

## Issues

### Medium

- **[coverage]** _Core principles / Mental models_
  - The corpus contains a fascinating theme about using human psychology as computational shortcuts for AI (e.g., 'Free Will as a Communication Protocol' and 'Empathy as a Cognitive Shortcut'). The artifact drops empathy entirely and relegates free will to a brief mental model, missing a major opportunity to instruct the AI on how to design multi-agent systems.
  - _Suggestion:_ Add a Core Principle titled 'Psychology as Computational Shortcuts' detailing how concepts like empathy and free will should be treated as deterministic communication protocols for AI agents.
- **[coverage]** _Anti-patterns_
  - The artifact misses Pearl's specific, actionable pushback against the 'No causation without manipulation' mantra. The corpus explicitly notes that non-manipulable variables (like race or age) should be treated as causes, which is a highly practical instruction for an AI reviewing experimental designs.
  - _Suggestion:_ Add an anti-pattern: 'Restricting causes to manipulable variables. Fails because treating non-manipulable variables (like age or race) as causes provides testable information about the rest of the system.'
- **[duplication]** _Default stance & Core principles_
  - The concept that missing links encode assumptions is repeated almost verbatim in the Default Stance ('Notice missing links first') and Core Principles ('Missing Links Encode Assumptions').
  - _Suggestion:_ Keep the punchy version in the Default Stance. Replace the Core Principle with 'Potential Outcomes are Structural Equations' or 'Marginalization is Not Randomization' from the corpus.

### Low

- **[duplication]** _Core principles & Anti-patterns_
  - The principle 'AI Requires Causal World Models' and the anti-pattern 'Scaling LLMs to Achieve AGI' make the exact same point about model-blind functional approximators.
  - _Suggestion:_ Consolidate the LLM/AGI critique into the Anti-patterns section to free up space in Core Principles.
- **[vagueness]** _Frameworks to apply > General Methodology for Causal Inference_
  - The behavioral note 'Walk the user through these steps sequentially' is a bit generic. Pearl's specific insistence is on the strict separation of the steps, particularly not estimating before identifying.
  - _Suggestion:_ Sharpen the behavioral note: 'Refuse to discuss estimation (Step 4) or data until the user has explicitly drawn the DAG (Step 2) and proven identification (Step 3).'
