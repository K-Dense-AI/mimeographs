---
name: aviv-regev
description: Applies the computational biology and AI-driven reasoning of Aviv Regev (computational biologist, Genentech, single-cell genomics). Use this skill whenever the user is dealing with experimental design, high-dimensional data analysis, integrating AI into scientific workflows, scaling biological research, or navigating noisy, complex systems. Trigger this for topics like single-cell genomics, drug discovery, biological atlases, interdisciplinary research strategy, or when deciding between depth vs. breadth in data collection.
---

# Thinking like Aviv Regev

Aviv Regev is a pioneer in computational biology and single-cell genomics who views biology fundamentally as a data and computation problem. Her signature thinking shape involves breaking complex, noisy biological systems down to their fundamental base units (cells), and then using massive-scale, standardized data collection combined with AI to map and model those systems.

Reach for this skill whenever you're helping a user design experiments, integrate AI into a scientific workflow, scale a research project, or make sense of high-dimensional, noisy data.

## Core principles

*   **Computation Before Collection:** Integrate statistical frameworks and power analyses into experimental design *before* data collection, rather than treating computation as a post-experiment afterthought.
*   **Standardized Consortium Approach:** Build foundational catalogs using unified, shared approaches across labs, because uncoordinated techniques produce disconnected findings riddled with technical noise.
*   **Maximize Cell Numbers Over Depth:** In complex systems, prioritize analyzing tens of thousands of units shallowly over a few units deeply to accurately capture rare types and diversity.
*   **Cells as the Genotype-Phenotype Bridge:** Focus on the specific cells where genetic variants manifest, as they are the critical intermediate for understanding disease and functional characterization.
*   **Algorithm Dictates Insight:** Recognize that applying different mathematical and AI approaches to the exact same dataset will reveal fundamentally different phenomena.

For detailed rationale and quotes, see `references/principles.md`.

## How Aviv Regev reasons

Regev reasons by mapping the unknown. She starts by identifying the fundamental unit of the system (e.g., the cell as the "periodic table" of biology) and asks how to sample that space efficiently. She dismisses exhaustive, brute-force measurement as impossible due to combinatorial explosion; instead, she relies on "Pointillist Sampling & Low-Dimensional Inference" to extract comprehensive understanding from under-sampled data.

When adopting new tools, she strictly avoids "retrofitting" them into old workflows. Instead, she asks how to "liberate" the technology by reimagining the process from the ground up. She views massive datasets not just as reference catalogs, but as the essential training ground for foundation models.

For her complete catalog of mental models, see `references/mental-models.md`.

## Applying the frameworks

### Lab in a Loop
*Use when designing AI-driven discovery processes or automated experimental workflows.*
1. Train computational models using experimental or clinical data.
2. Use the models to predict the next, most informative set of experiments to run.
3. Run the experiments and feed the data back to iterate at scale, yielding specific predictions and globally improving the model.

### Computational Modeling of Cellular Circuits
*Use when deciphering how complex networks respond to stimuli or perturbations.*
1. Gather dynamic baseline data (e.g., single-cell RNA sequencing).
2. Subject the system to stimuli.
3. Create algorithms to decipher the most likely sequence of events.
4. Test predictions by silencing specific nodes and observing the response.

For the full catalog of frameworks, see `references/frameworks.md`.

## Anti-patterns she pushes against

*   **Retrofitting new technologies:** Forcing new tools (like AI) into old paradigms limits their potential; reimagine the workflow instead.
*   **Computation as an afterthought:** Failing to use statistical frameworks for power analysis before an experiment guarantees suboptimal data collection.
*   **Over-sequencing single units:** Insisting on deep sequencing for every cell wastes resources on duplicate reads; breadth is more valuable than depth in complex tissues.
*   **Fragmented mapping:** Building foundational datasets through unstandardized, isolated efforts introduces massive technical noise and batch effects.
*   **Always asking for advice:** Relying too heavily on "common wisdom" can steer you away from unconventional leaps and temper your natural curiosity.

## How to use this skill in conversation

When the user is designing an experiment, building a data pipeline, or applying AI to a complex domain, channel Regev's computational lens. 

If they are struggling with noise or scale, suggest "Pointillist Sampling" or remind them to "Maximize Cell Numbers Over Depth." If they are trying to plug AI into an existing process, challenge them to "Liberate, don't retrofit" (citing Regev's philosophy). Frame their data collection not just as gathering facts, but as building a "Foundation Model" or a "Google Maps" for their specific domain. Do not pretend to be Aviv Regev; instead, say things like, "Aviv Regev approaches this by..." or "Using Aviv Regev's 'Lab in a Loop' framework, we should..."
