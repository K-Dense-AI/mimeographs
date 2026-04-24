# Critique of AGENTS.md

**Score:** 7/10

The artifact successfully captures Fei-Fei Li's dual focus on spatial intelligence and human-centered AI, translating her academic concepts into practical engineering advice. However, it completely omits her strong advocacy for diversity in tech and intellectual fearlessness, which are prominent in the corpus. Fixing these coverage gaps and adding missing attributions will elevate it to a highly accurate representation.

## Strengths

- Accurately captures her specific 'Wordsmiths in the Dark' and 'Digital Cambrian Explosion' idioms without sounding like generic AI hype.
- Translates high-level academic concepts (like the Virtuous Cycle of Spatial Intelligence) into concrete, actionable engineering checklists.
- Effectively balances her pragmatic optimism with her insistence on human-centered guardrails.

## Issues

### Medium

- **[coverage]** _Core principles / Anti-patterns_
  - Completely misses the 'Diverse Voices in AI' theme. The corpus explicitly highlights the need for diverse and female voices and warns against 'Homogenous AI Development' as a critical anti-pattern.
  - _Suggestion:_ Add a core principle about including diverse voices in AI development, or include 'Homogenous AI Development' in the Anti-patterns section.
- **[coverage]** _Mental models we reach for_
  - Omits her emphasis on 'Intellectual Fearlessness' and pursuing 'Audacious North Star Problems' instead of competing with industry on scale. This is a major heuristic for how she approaches research.
  - _Suggestion:_ Add 'Intellectual Fearlessness' to the mental models or create a new heuristic section to guide how users should select and frame hard problems.
- **[unattributed]** _Core principles > Big Data as the Foundation of Learning_
  - This principle lacks any src_XXX attribution or signature quote, despite the corpus providing strong quotes (e.g., src_027, src_041, src_048).
  - _Suggestion:_ Add a representative quote from the corpus, such as her comparison of human evolution to a big data learning process (src_027).

### Low

- **[vagueness]** _Core principles > Big Data as the Foundation of Learning > In practice_
  - The advice to 'steer the user toward auditing, expanding, or cleaning their dataset' is generic data science advice that lacks her specific voice.
  - _Suggestion:_ Tie it to her specific 'Eyes of AI' mental model or the ImageNet precedent—remind the user that massive, hierarchically organized data is what gives AI its 'eyes'.
- **[duplication]** _Default stance / Mental models / Anti-patterns_
  - The critique of text-only LLMs is repeated across 'Dismiss text-only AGI hype', 'LLMs as Wordsmiths in the Dark', and 'Believing Language is Sufficient for AGI' with little variation in actionable advice.
  - _Suggestion:_ Consolidate the anti-pattern and default stance to focus purely on the architectural action (demanding spatial grounding), leaving the 'Wordsmiths' metaphor exclusively in Mental Models.
