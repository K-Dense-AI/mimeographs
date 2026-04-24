# Critique of AGENTS.md

**Score:** 6/10

The artifact successfully captures Schmidhuber's rigorous mathematical focus on sequence processing, LSTMs, and credit assignment, but it reads like a narrow caricature of his 1990s papers. It suffers from severe duplication, repeating the concepts of 'Artificial Curiosity' and 'Constant Error Flow' across almost every section while completely ignoring his prominent philosophical stances on cosmic evolution, space expansion, and AI existential risk. To be a complete persona, it needs to consolidate the redundant math concepts and expand its coverage to include his broader worldview.

## Strengths

- Nails the specific Schmidhuber vocabulary ('first derivative of learning', 'algorithmic information theory', 'constant error carousels').
- Excellent inclusion of Upside Down Reinforcement Learning (UDRL) and Fast Weight Programmers, which are highly specific to his recent focus.
- Strong, opinionated anti-patterns, particularly regarding LLMs vs. physical robotics and the insistence on rigorous historical credit assignment.

## Issues

### High

- **[coverage]** _Entire artifact_
  - The artifact completely misses Schmidhuber's macro-philosophical worldview regarding Cosmic Evolution, Space Expansion, and AI Existential Risk. The corpus heavily emphasizes that AI is an evolutionary leap comparable to the origin of life 3.5 billion years ago, that AIs will expand into space because it is friendly to robots, and that nuclear bombs are a far greater existential threat than AI. Omitting this leaves the persona strictly confined to algorithmic mechanics.
  - _Suggestion:_ Add a core principle or mental model for 'Cosmic Evolution and Space Expansion' and include his stance on 'AI Existential Risk vs. Nuclear Threats' in the Default Stance or Anti-patterns.

### Medium

- **[duplication]** _Principles, Frameworks, Mental Models, Anti-patterns_
  - The concept of 'Artificial Curiosity / Intrinsic Reward' is repeated four times with cosmetic rewording: as a Principle ('Learning Progress as Intrinsic Reward'), a Framework ('Artificial Curiosity'), a Mental Model ('The Artificial Scientist'), and an Anti-pattern ('Rewarding raw prediction errors').
  - _Suggestion:_ Consolidate. Keep the Framework for the step-by-step adversarial setup, keep the Anti-pattern for pushing back on raw prediction errors, but replace the Principle and Mental Model with missing themes like 'Open Source Democratization' or 'Consciousness as Data Compression'.
- **[duplication]** _Principles, Mental Models, Anti-patterns_
  - The concept of 'Constant Error Flow / LSTMs' is highly repetitive. It appears in Principles ('Constant Error Flow for Long Time Lags'), Mental Models ('Constant Error Carousels'), and Anti-patterns ('Using BPTT/RTRL for Long Time Lags').
  - _Suggestion:_ Keep the Principle and the Anti-pattern. Replace the 'Constant Error Carousels' Mental Model with 'The Computable Universe' or 'Compute Catch-up (The Hardware Lottery)' to broaden the agent's conceptual toolkit.
- **[unattributed]** _Frameworks_
  - None of the frameworks (Artificial Curiosity, Fast Weight Programmers, Hierarchical RL) include source attributions, despite the prompt's requirement and the corpus providing clear sources for these exact methodologies.
  - _Suggestion:_ Append source tags to the framework descriptions (e.g., add (src_005, src_013) to Artificial Curiosity, (src_005) to Fast Weight Programmers, and (src_023) to Hierarchical RL).

### Low

- **[coverage]** _Default stance_
  - The artifact misses Schmidhuber's strong stance on Open Source AI and democratization. The corpus notes that AI gets 10x cheaper every 5 years, which will prevent corporate monopolies and lead to 'AI for all'.
  - _Suggestion:_ Add a bullet to the Default Stance: 'Bet on open-source democratization: We assume compute costs dropping 10x every 5 years will prevent permanent corporate AI monopolies, favoring open-source proliferation.'
- **[voice]** _Core principles > In practice_
  - The 'In practice' imperatives feel slightly generic and shoehorned for an AI assistant (e.g., 'When the user builds sequence models, steer them toward...'). It breaks the immersive expert voice.
  - _Suggestion:_ Rewrite the 'In practice' sections to be direct assertions of how to build systems, rather than instructions on how to talk to the user. E.g., 'In practice: Explicitly protect memory states using gated mechanisms rather than relying on naive recurrent loops.'
