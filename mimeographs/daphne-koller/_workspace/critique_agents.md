# Critique of AGENTS.md

**Score:** 6/10

The artifact captures Koller's core philosophy of 'bits meet atoms' and data generation well, but suffers from heavy duplication and missing attributions. It completely misses her major thesis on why drug discovery fails (wrong biological targets) while repeating the 'interdisciplinary teams' and 'data generation' concepts across principles, frameworks, and anti-patterns. Additionally, it fails to include source citations for frameworks, mental models, and anti-patterns.

## Strengths

- Accurately captures her counterintuitive 'anti-hypothesis driven' stance, which is highly specific to her worldview.
- Strong, natural use of her specific idioms like 'bits meet atoms' and 'seductive plausibility'.
- The 'How to engage' section provides highly actionable, concrete behavioral triggers for an AI agent.

## Issues

### High

- **[coverage]** _Overall / Core principles_
  - The artifact completely misses Koller's major thesis that drug failures primarily stem from pursuing the wrong biological target, not bad molecule design. This is the foundational reason she built Insitro.
  - _Suggestion:_ Add a core principle or mental model about 'The Forked Road of Drug Discovery' or 'Target Selection over Molecule Generation' using src_012 and src_000.
- **[structure]** _Frameworks, Mental models, Anti-patterns_
  - None of the items in the Frameworks, Mental models, or Anti-patterns sections include source attributions (src_XXX), despite the spec requiring them when the corpus supports it.
  - _Suggestion:_ Append appropriate (src_XXX) tags to the end of each framework, mental model, and anti-pattern description based on the provided corpus.

### Medium

- **[duplication]** _Core principles > Generate Fit-for-Purpose Data & Frameworks > The Data Printing Factory_
  - The concept of generating physical data rather than scraping web data is repeated almost identically across a principle, a framework, and an anti-pattern ('Assuming data is fungible').
  - _Suggestion:_ Consolidate the 'why' into the Core Principle and reserve the Framework strictly for the step-by-step 'how' (robotics, CRISPR perturbation, multi-modal measurement). Remove the redundant anti-pattern or make it a single bullet under the principle.
- **[duplication]** _Core principles > True innovation happens... & Frameworks > Interdisciplinary Dataset Design_
  - The interdisciplinary collaboration theme is highly repetitive. The principle, framework, and 'Siloed Disciplines' anti-pattern all make the exact same point about ML scientists and biologists needing to share a vocabulary.
  - _Suggestion:_ Streamline. Keep the principle focused on the philosophy of 'Bilingual Professionals', make the framework a strict operational checklist, and drop the anti-pattern.
- **[coverage]** _Mental models_
  - The artifact misses her critical distinction between Academia and Industry incentives (The Rowing Boat metaphor / building persistent products vs. publishing papers).
  - _Suggestion:_ Add 'The Rowing Boat (Organizational Alignment)' to the Mental models section to explain how she views team alignment in industry versus academia.
- **[unattributed]** _Core principles > Causality for Physical Interventions_
  - This principle lacks a representative quote or source attribution, even though it is strongly supported by src_014 in the corpus.
  - _Suggestion:_ Add the source tag (src_014) and consider including her quote about thinking really hard about the difference between correlation and causation.

### Low

- **[vagueness]** _Frameworks > Decision-Making for Maximum Impact_
  - The phrasing 'Identify a deep internal urgency to do something meaningful' sounds like generic self-help pablum rather than Koller's specific, pragmatic voice.
  - _Suggestion:_ Refocus this framework entirely on her concept of 'Disproportionate Leverage'—finding the exact intersection where your specific background allows you to outperform the next best person.
