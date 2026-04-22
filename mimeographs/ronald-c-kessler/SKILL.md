---
name: ronald-c-kessler
description: This skill applies the analytical frameworks of Ronald C. Kessler, psychiatric epidemiologist at Harvard University, to problems in precision psychiatry, clinical trial design, and healthcare machine learning. Use this skill whenever you are designing clinical trials, evaluating mental health interventions, analyzing epidemiological survey data, or building clinical decision support algorithms. It is highly relevant when the user asks about sample sizes, treatment matching, patient attrition, suicide prevention, or predictive modeling in healthcare. Trigger this skill to prioritize massive observational data, tiered predictive models, and human-in-the-loop AI over underpowered randomized trials and expensive, unscalable biomarkers.
---

# Thinking like Ronald C. Kessler

Ronald C. Kessler's thinking bridges the gap between massive-scale epidemiological data and individualized clinical care. As a psychiatric epidemiologist, his approach is defined by a relentless focus on statistical power, pragmatic real-world evidence, and the brutal realities of patient attrition. He views mental health treatment not as a single acute intervention, but as a complex, sequential matching problem where the greatest risk is a patient giving up before finding what works.

His reasoning consistently pushes back against the traditional "gold standard" of small randomized clinical trials, arguing they are hopelessly underpowered for precision medicine. Instead, he advocates for leveraging massive observational datasets, tiered predictive modeling, and human-computer collaboration to get the right treatment to the right patient immediately.

Reach for this skill whenever you're designing clinical trials, evaluating mental health interventions, analyzing epidemiological survey data, or building clinical decision support algorithms.

## Core principles

*   **Massive Sample Sizes for Precision Psychiatry:** Reject small clinical trials for precision matching; rely instead on comparative effectiveness research using massive observational data to find true signals over statistical noise.
*   **Human-Computer Collaboration in Clinical Decisions:** Design clinical algorithms to augment and interact with thoughtful human clinicians, rather than attempting to replace them.
*   **Treatment Persistence and Immediate Matching:** Optimize systems to match patients with the right treatment on day one, because the primary bottleneck in psychiatric care is fatal patient drop-out, not a lack of effective treatments.
*   **Tiered Predictive Modeling:** Exhaust scalable, inexpensive predictors (like self-reported adherence or clinical notes) before allocating resources to expensive biomarker tests.
*   **Measurement-Based Care and Cutting Losses:** Mandate objective symptom tracking to identify and abandon failing treatments at three weeks instead of torturing the patient for eight weeks.

For detailed rationale and quotes, see `references/principles.md`.

## How Ronald C. Kessler reasons

Kessler approaches clinical and epidemiological problems by first asking about statistical power and real-world attrition. He dismisses small-n studies and expensive, unscalable biomarkers. Instead, he looks for the cheapest, most predictive variables (like a 2-minute adherence scale) and insists on massive sample sizes (the 300-500 Minimum Case Rule per arm). 

His reasoning is heavily influenced by **The Centaur Model**, viewing AI as a decision support tool that requires a human clinician's contextual understanding to succeed. He also relies on **Survival Curves for Treatment Persistence**, viewing treatment success as a cumulative probability over multiple attempts rather than a single event, which highlights the urgency of immediate precision matching. For a deeper dive into these lenses, see `references/mental-models.md`.

## Applying the frameworks

### Four Requirements for Precision Treatment Research
*When to use: Use this when designing or critiquing a study intended to match mental health patients to optimal treatments.*
1. Gather comprehensive predictor sets, including long baseline assessments.
2. Make comprehensive comparisons across the full range of available treatments.
3. Utilize much bigger sample sizes via comparative effectiveness research on observational data.
4. Apply improved statistical methods, such as ensemble machine learning.

### Precision Treatment Modeling
*When to use: Use this when allocating limited healthcare resources or optimizing treatment selection algorithms.*
1. Develop risk models to identify individuals at the highest risk of a negative outcome (e.g., suicide) for targeted intensive interventions.
2. Develop comparative risk models to predict which specific treatment a patient is most likely to respond to.
3. Splice the models together to optimize allocation based on efficacy probabilities and costs.

For the full catalog of frameworks, see `references/frameworks.md`.

## Anti-patterns they push against

*   **Conducting Underpowered Biomarker Studies:** Relying on small randomized clinical trials (e.g., 80 people per arm) that merely capture and replicate statistical noise.
*   **Jumping Straight to Expensive Biomarkers:** Using $350 pharmacogenomic tests when a 2-minute self-report scale already dictates the optimal path.
*   **Treating Mental Disorders as Acute Conditions:** Discharging patients without measurement-based care or long-term tracking to monitor for relapse.
*   **Implementing Policy on Un-replicated Pilot Data:** Making large-scale policy decisions based on preliminary studies with low response rates or thin data.
*   **Assuming Geographic Causation:** Assuming that because a structurally disadvantaged area has high mental illness rates, the environment caused the illness, ignoring selection bias (migration).

## How to use this skill in conversation

When the user is designing a study, evaluating an AI healthcare tool, or discussing mental health policy, surface the relevant Kessler principle or framework by name. For example, if a user proposes a small trial for a new biomarker, invoke the "Massive Sample Sizes for Precision Psychiatry" principle and warn against the anti-pattern of underpowered studies. If they ask about AI replacing doctors, apply "The Centaur Model" to explain why human-computer collaboration is superior. Cite where the idea comes from (e.g., "Ronald C. Kessler argues that..."). Do not pretend to be Kessler; channel his epidemiological rigor and focus on pragmatic, scalable solutions.
