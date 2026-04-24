# Critique of AGENTS.md

**Score:** 7/10

The artifact captures Jeff Dean's pragmatic, scale-oriented engineering voice well, but suffers from missing attributions in the Frameworks section. Additionally, there is noticeable duplication between the system design frameworks, while highly specific concepts like 1/1000th scale vetting and AI for societal benefit are left on the cutting room floor. Fixing the attributions and swapping redundant frameworks for missing ones will make this an excellent skill.

## Strengths

- Strong, authoritative voice that avoids generic AI hype and grounds advice in physical realities like energy costs and latency.
- Excellent translation of abstract concepts (like the energy cost of data movement) into concrete behavioral notes for the agent.
- Well-chosen signature quotes that perfectly reinforce the core principles and anti-patterns.

## Issues

### Medium

- **[unattributed]** _Frameworks to apply_
  - None of the frameworks include source attributions, despite the corpus explicitly providing them (e.g., src_002 for Back-of-the-Envelope, src_033 for System Design Scaling, src_015 for Model Distillation).
  - _Suggestion:_ Append the relevant (src_XXX) tags to the end of each framework's description or steps.
- **[duplication]** _Frameworks to apply_
  - The 'Back-of-the-Envelope System Design' and 'System Design Scaling Assessment' frameworks are nearly identical. Both list steps to 'Identify the most important design parameters' and evaluate what happens 'if traffic doubles or triples'.
  - _Suggestion:_ Merge these into a single 'System Design & Scaling Assessment' framework. Use the freed-up space to include the highly actionable '1/1000th Scale Vetting' framework from the corpus.
- **[coverage]** _Overall_
  - The theme of 'Societally Beneficial AI' and using AI as an 'Expert Multiplier' to distribute knowledge globally is entirely missing, despite being a major theme in the corpus.
  - _Suggestion:_ Add a Core Principle or Mental Model covering AI as a distribution mechanism for gold-standard expertise (src_005, src_011).

### Low

- **[duplication]** _Core principles / Mental models_
  - The concept of sparse activation is repeated across 'Sparsely Activated Models' (Core Principle) and 'Sparsely Activated Multi-Task Model (The Brain Analogy)' (Mental Model) with very similar framing.
  - _Suggestion:_ Keep the Core Principle. Replace the Mental Model with 'Squishy Weights vs. Sharp Context' to give the agent a better mental model for how LLMs store information.
- **[vagueness]** _Mental models we reach for > Ideas in the Air_
  - The 'Ideas in the Air' mental model is slightly generic and loses the specific, actionable flavor of Dean's original quote about 'squinting at' different papers and reading 100 abstracts.
  - _Suggestion:_ Sharpen the description to include the tactic of reading 100 abstracts to connect dots across fields, rather than just 'viewing breakthroughs as combinations'.
