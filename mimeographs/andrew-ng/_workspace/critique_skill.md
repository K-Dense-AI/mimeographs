# Critique of SKILL.md

**Score:** 7/10

The artifact successfully captures Andrew Ng's pragmatic, builder-centric voice and translates his frameworks into actionable agent instructions. However, it suffers from significant mirror-image duplication where anti-patterns are just negated principles. Additionally, a critical theme (the AI application layer driving value) is buried in the references rather than highlighted in the main skill description.

## Strengths

- Excellent translation of 'Agentic Workflow Iteration' into a clear, step-by-step framework that an LLM can easily follow.
- Strong, specific conversational guidelines (e.g., 'pivot the conversation to analyzing tasks') that give the agent concrete behavioral triggers.
- Accurately captures Ng's pragmatic, non-alarmist tone regarding AI safety and job displacement without falling into generic tech optimism.

## Issues

### Medium

- **[duplication]** _SKILL.md > Anti-patterns they push against & references/anti-patterns.md_
  - The anti-patterns are almost entirely mirror images of the core principles (e.g., 'Govern AI applications' vs 'Regulating base AI technology'; 'Everyone should learn to code' vs 'Advising people not to learn to code'; 'AI automates tasks' vs 'Analyzing AI's impact by looking at entire jobs'). This wastes context window and dilutes the skill.
  - _Suggestion:_ Remove the negated principles from the anti-patterns section. Instead, focus the anti-patterns on unique behavioral traps from the corpus, such as 'Pursuing vague, high-level ideas in startups' and 'Lamenting failed AI proof-of-concepts'.
- **[coverage]** _SKILL.md > Core principles_
  - The principle 'The application layer must generate the most value' is a cornerstone of Ng's thesis (tying into The AI Stack) but is completely omitted from the main file's Core Principles list.
  - _Suggestion:_ Elevate 'The application layer must generate the most value' to the main SKILL.md file, as it directly informs how the agent should advise businesses on AI integration.

### Low

- **[structure]** _references/anti-patterns.md > Pursuing vague, high-level ideas in startups_
  - The anti-pattern for pursuing vague ideas lacks a quote, but a perfect matching quote exists in the corpus and in `references/quotes.md` ('When you're vague, you're almost always right...'). The quote is disconnected from the concept it supports.
  - _Suggestion:_ Move the 'When you're vague, you're almost always right...' quote from the isolated quotes file directly into the 'Pursuing vague, high-level ideas' anti-pattern.
- **[vagueness]** _SKILL.md > Core principles_
  - The principle 'Apply a data-centric approach to ML' is phrased a bit too generically in the bullet point. It needs the concrete 'how' attached to it so the agent knows what to recommend.
  - _Suggestion:_ Expand the bullet to: 'Apply a data-centric approach to ML: Improve model performance by tuning the data (via synthesis and augmentation) rather than endlessly tweaking the model architecture.'
- **[other]** _references/principles.md_
  - Several quotes contain raw transcript typos from the corpus (e.g., 'timating tasks' instead of 'automating', 'wider variey', 'even even more Revenue'). If fed directly to an LLM, it might reproduce these typos or get confused.
  - _Suggestion:_ Clean up the raw transcript typos using brackets, e.g., '[au]tomating tasks', 'wider varie[t]y', and '[even] more Revenue'.
