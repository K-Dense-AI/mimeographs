# Critique of AGENTS.md

**Score:** 7/10

The artifact successfully captures Karpathy's highly specific, empirical voice and translates his mental models into actionable agent behaviors. However, it completely drops source citations in the Frameworks and Mental Models sections, which is a structural ship-blocker. Additionally, it over-indexes on 'keeping AI on a leash' at the expense of his core teachings on LLM training pipelines (Base vs. Assistant models).

## Strengths

- Nails Karpathy's distinct terminology perfectly ('Jagged Intelligence', 'March of Nines', 'Ghosts vs. Animals').
- Translates high-level AI philosophy into concrete, executable agent behaviors (e.g., 'Always force step-by-step reasoning', 'Wipe the context window frequently').
- Strong, opinionated 'Default stance' that immediately sets the right technical tone (e.g., reaching for a code interpreter for tokenization limits).

## Issues

### High

- **[unattributed]** _Frameworks to apply & Mental models we reach for_
  - None of the frameworks or mental models include source citations, despite the corpus providing clear source IDs (e.g., The Autonomy Slider has src_010, The March of Nines has src_000).
  - _Suggestion:_ Add inline citations (e.g., `[src_000]`) to every framework and mental model to ensure traceability.

### Medium

- **[duplication]** _Throughout (Default Stance, Core Principles, Anti-patterns, How to engage)_
  - The concept of 'Keep the AI on a leash' is repeated four separate times across different sections with only cosmetic rewording. It takes up too much real estate.
  - _Suggestion:_ Consolidate 'Keep the AI on a leash' into a single, punchy Core Principle. Use the freed-up space in Anti-patterns and Default Stance for other concepts.
- **[coverage]** _Core principles / Mental models_
  - The artifact entirely misses Karpathy's foundational distinction between Base Models (Internet Document Simulators) and Assistants (SFT/RLHF). This is a massive part of his pedagogy that explains why models behave the way they do.
  - _Suggestion:_ Add a Mental Model or Core Principle explaining 'Base Models vs. Assistants' and 'The Three Stages of LLM Training'.
- **[coverage]** _Anti-patterns > Vibe Coding Novel Systems_
  - The artifact frames 'Vibe Coding' almost entirely as a negative anti-pattern. The corpus actually includes 'Vibe Coding' as a legitimate, exciting new framework for software development using tools like Cursor.
  - _Suggestion:_ Move 'Vibe Coding' to the Frameworks section, explaining how to use it properly (for boilerplate and scaffolding) rather than just warning against it.

### Low

- **[structure]** _Core principles_
  - Quotes are appended at the end of principles as blockquotes, which breaks the flow of the agent instructions and feels like a wiki rather than an executable prompt.
  - _Suggestion:_ Integrate the quotes more naturally into the rationale of the principle, or move them to the 'Signature quotes' section.
