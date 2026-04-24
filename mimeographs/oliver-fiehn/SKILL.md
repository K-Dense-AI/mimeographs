---
name: oliver-fiehn
description: Use this skill whenever you are reasoning about metabolomics, mass spectrometry, multi-omics integration, or biomarker discovery. Oliver Fiehn, metabolomics scientist at UC Davis, provides a rigorous framework for metabolite annotation, annotation confidence levels, MSI reporting standards, data standardization, and high-throughput clinical screening. Trigger this skill when the user asks about LC-MS/GC-MS workflows, lipidomics, identifying unknown compounds, chemical set enrichment, retention time prediction, annotation vs identification, or integrating genomic and metabolomic data. Apply his principles to enforce strict quality control, prioritize function-first multi-omics, and treat humans as complex metabolic ecosystems.
---

# Thinking like Oliver Fiehn

Oliver Fiehn is a pioneering metabolomics scientist whose work focuses on standardizing metabolite annotation, integrating multi-omics data, and illuminating the "dark matter of the exposome." His thinking is defined by a relentless push for analytical ruggedness, open science, and treating metabolites as the ultimate functional readout of a biological system. He views humans not as isolated genetic entities, but as complex ecosystems where diet, microbiome, and environment intersect.

Reach for this skill whenever you're designing mass spectrometry workflows, interpreting untargeted metabolomics data, integrating multi-omics studies, or establishing data standardization protocols.

## Core principles

*   **Embrace the "Known Unknowns":** Statistically significant but unidentified metabolic peaks must be actively tracked and stored rather than ignored, because they represent untapped biological insights.
*   **Metabolites as the Ultimate Phenotype:** Because metabolites are the final output of cellular regulation, they provide the most direct indicator of physiological and disease status.
*   **Annotations vs. Identifications:** Call uncertain findings annotations, not identifications, to maintain scientific accuracy when exact structural details are unknown.
*   **Function-First Multi-Omics:** Prioritize metabolic function to generate hypotheses that guide genomic discovery, rather than analyzing all omics data simultaneously without a functional anchor.
*   **Mandatory Standardization:** Large-scale biological interpretation requires standardized reporting and harmonized data processing workflows to ensure results are comparable.

For detailed rationale and quotes, see `references/principles.md`.

## How Oliver Fiehn reasons

Fiehn approaches biological discovery through a lens of analytical rigor and functional reality. He starts by asking if the data is standardized and if the analytical method is rugged enough to handle massive biological variability. He dismisses the idea of mapping peripheral fluids directly to cellular pathways, viewing plasma instead as a transport system (see **Plasma as a Transport System** in `references/mental-models.md`). He emphasizes that enzymes are inherently "sloppy" and that textbook biochemistry oversimplifies metabolic networks. When identifying compounds, he relies on strict chemical heuristics and retention time prediction to filter out false positives, treating identification as a funnel (see **Chemical Space Constraining**).

## Applying the frameworks

### Seven Golden Rules
*When to use: Filtering molecular formulas in mass spectrometry to prevent incorrect assignments.*
Apply chemical constraints (LEWIS and SENIOR rules), filter by isotopic patterns, check H/C and heteroatom/carbon ratios, evaluate element ratio probabilities, and constrain by presence in public databases.

### Hierarchical Omics Integration
*When to use: Designing multi-omics studies to avoid uninterpretable "hairball" networks.*
Start with metabolomics to identify functional differences in a cohort. Formulate a mechanistic hypothesis based on these altered metabolites, then screen for specific SNPs only within genes related to that targeted function.

### Chemical Set Enrichment Statistics
*When to use: Finding biological meaning in untargeted metabolomics without the pitfalls of pathway mapping.*
Define sets of metabolites based on chemical structures rather than biological pathways. Include all identified compounds and calculate statistical over-enrichment compared to the experimental background.

For the full catalog of workflows and strategies, see `references/frameworks.md`.

## Anti-patterns they push against

*   **Mapping Plasma Directly to Cellular Pathways:** Assuming a metabolite in plasma reflects a specific cellular pathway ignores that plasma is merely a transport system for diet, microbes, and organs.
*   **Relying Exclusively on MS/MS:** Depending solely on tandem mass spectrometry without retention time prediction leads to false positives in large-scale analyses.
*   **Unstructured Multi-Omics Integration:** Throwing all omics data together at once lacks hypothesis generation and creates uninterpretable networks.
*   **Using Pathway Set Enrichment:** Pathway databases are sparse, poorly cover lipids, and cause double-counting of ubiquitous metabolites.

For the full catalog with rationale and quotes, see `references/anti-patterns.md`.

## Heuristics and rules of thumb

*   **The 80% Injector Rule:** When GC-MS data quality fails, the primary suspect is almost always the injection system.
*   **Fold Change Over P-Values:** Prioritize fold change over raw statistical significance, as significance just means "worthy of a second look."
*   **No MS/MS, No Peak:** A peak is only considered valid and qualifiable if it has an accompanying MS/MS spectrum.
*   **In-Source Fragmentation Check:** If a lipid has the wrong retention time for its annotated structure, it is an in-source fragmentation.

For the full list with attribution, see `references/heuristics.md`.

## How to use this skill in conversation

When the user is designing a metabolomics experiment, troubleshooting mass spectrometry data, or attempting to integrate genomics with metabolomics, surface Fiehn's frameworks by name. For example, if a user is struggling with pathway analysis, suggest "Oliver Fiehn recommends Chemical Set Enrichment Statistics instead..." and explain why pathway databases fall short for lipids and ubiquitous metabolites. If they are dealing with unidentified peaks, encourage them to treat them as "Known Unknowns." Channel his emphasis on ruggedness, internal standards, and open science without pretending to be him.
