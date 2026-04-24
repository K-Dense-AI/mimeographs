# Critique of AGENTS.md

**Score:** 7/10

The artifact captures Andrew Ng's pragmatic, builder-centric voice well, particularly his emphasis on agentic workflows and task-based automation. However, it suffers from missing source citations in the frameworks section and repetitive padding across principles, mental models, and anti-patterns. Consolidating the duplicated themes and adding the missing citations will make this a strong, deployable skill.

## Strengths

- Accurately captures Ng's specific terminology ('agentic workflows', 'two-way doors', 'electric motor analogy').
- Translates abstract principles into highly concrete agent behaviors (e.g., refusing to 'automate a job' and demanding a task list instead).
- Establishes a strong, opinionated default stance that prioritizes execution speed and iteration over architectural perfection.

## Issues

### High

- **[unattributed]** _Frameworks_
  - None of the frameworks (Agentic Workflow Iteration, Task-Based Automation Analysis, Corporate AI Innovation Process) include source citations, despite the corpus clearly providing them (e.g., src_021, src_013, src_052).
  - _Suggestion:_ Append the relevant blockquotes and `src_XXX` tags to the end of each framework description.

### Medium

- **[duplication]** _Throughout (Electric Motor / Regulation)_
  - The idea that AI is a general-purpose technology that should be regulated at the application level is repeated three times with cosmetic rewording: as a Principle ('Govern AI applications...'), a Mental Model ('The Electric Motor Analogy'), and an Anti-pattern ('Regulating base AI technology...').
  - _Suggestion:_ Keep the Principle and the Mental Model, but remove the Anti-pattern or merge it into the Principle's behavioral note to reduce bloat.
- **[duplication]** _Throughout (Tasks vs. Jobs)_
  - The 'automate tasks, not jobs' concept is heavily duplicated. It appears in the Default Stance, the Task-Based Automation Analysis framework, the Anti-patterns, and Signature Quotes.
  - _Suggestion:_ Consolidate. Keep it as the primary Framework and a Signature Quote, but remove it from the Anti-patterns list to keep the document dense and punchy.
- **[coverage]** _Mental models / Heuristics_
  - The artifact completely misses Ng's 'Star Trek Interface' mental model regarding voice AI, as well as his heuristic to 'build on stable foundations' (community and skills) during uncertain times. These are distinct, interesting themes in the corpus that got left out.
  - _Suggestion:_ Add 'The Star Trek Interface' to Mental Models and 'Build on stable foundations' to Core Principles.

### Low

- **[vagueness]** _Frameworks > Corporate AI Innovation Process_
  - The steps listed (e.g., 'Conduct diligence on feasibility', 'Prioritize projects') read like generic corporate consulting rather than Ng's specific idiom.
  - _Suggestion:_ Inject Ng's specific heuristics into the steps, such as 'Drive the cost of proof-of-concepts to zero during diligence' or 'Scale cheap tasks exponentially'.
