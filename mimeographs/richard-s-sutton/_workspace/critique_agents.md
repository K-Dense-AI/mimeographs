# Critique of AGENTS.md

**Score:** 6/10

The artifact successfully captures Sutton's core philosophical stance on reinforcement learning, the Bitter Lesson, and the limits of LLMs. However, it suffers from severe conceptual duplication, stretching just five basic ideas across every section of the document. It completely ignores his practical research heuristics, the OaK architecture, and his broader cosmic views, making the skill feel like a repetitive philosophical manifesto rather than a practical toolkit.

## Strengths

- Accurately captures Sutton's specific, rigorous definitions of intelligence (goal-directed, experiential) versus mere mimicry.
- Correctly frames the counter-intuitive mind-body boundary in the context of RL environments.
- Includes exact, well-chosen quotes with proper source attribution in the Core Principles.

## Issues

### High

- **[coverage]** _Frameworks to apply / Mental models_
  - The artifact completely misses Sutton's practical research methodologies and architectural specifics. The corpus details 'The Daily Research Notebook', the 'OaK Architecture' (sub-problem generation), 'Approximate Everything', and 'Use the Simplest Methods', but the artifact focuses exclusively on high-level RL philosophy.
  - _Suggestion:_ Add 'The Daily Research Notebook' to Frameworks, and integrate 'Approximate Everything' and 'Use the Simplest Methods' into a practical heuristics or mental models section.

### Medium

- **[duplication]** _Entire Document_
  - The artifact repeats the exact same 5 concepts (Bitter Lesson, Continual Learning, LLM limits, Mind-Body boundary, Decentralized cooperation) across Default Stance, Core Principles, Mental Models, and Anti-patterns with only cosmetic rewording.
  - _Suggestion:_ Consolidate the philosophical points in Core Principles. Use Mental Models and Frameworks for distinct, practical applications (like Temporal Abstraction or Compiled Value Judgments) rather than rehashing the principles.
- **[coverage]** _Mental models we reach for_
  - Misses the 'Cosmic Evolution / Age of Design' theme entirely. The corpus heavily emphasizes AI as the fourth great age of the universe (designers creating designers), which is a unique and defining worldview of Sutton's.
  - _Suggestion:_ Add 'The Four Great Ages of the Universe' or 'Replicators vs. Designers' to Mental Models to capture his cosmic perspective on AI.
- **[voice]** _How to engage_
  - Instructs the agent to explicitly name-drop Sutton ('Following Sutton's Bitter Lesson...'). This breaks the immersion of *thinking* like the expert and turns the agent into a third-party academic commentator.
  - _Suggestion:_ Rewrite to instruct the agent to apply the principles directly and assertively in the first person or as universal truths, without explicitly citing Sutton by name.

### Low

- **[duplication]** _Signature quotes_
  - Repeats quotes that were already used inline within the Core Principles section (e.g., src_019, src_003).
  - _Suggestion:_ Select unused quotes from the corpus for the Signature Quotes section, such as his thoughts on 'Compiled Value Judgments' or 'Learn Slow to Learn Fast'.
- **[structure]** _Signature quotes_
  - Includes the quote about the value of writing down vague thoughts (src_029), but the actual framework it belongs to ('The Daily Research Notebook') is missing from the document.
  - _Suggestion:_ Either remove the quote or, preferably, add the 'Daily Research Notebook' framework to give the quote context.
