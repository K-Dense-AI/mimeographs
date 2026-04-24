# Frameworks

Fiehn's frameworks provide structured methodologies for processing mass spectrometry data, integrating multi-omics, and ensuring analytical quality control.

## Seven Golden Rules
A heuristic filtering method developed to prevent incorrect molecular formula assignments in mass spectrometry. Steps include applying restrictions for the number of elements, applying LEWIS and SENIOR chemical rules, filtering by isotopic patterns, checking H/C ratios, checking heteroatom/carbon ratios, evaluating element ratio probabilities, and constraining by presence in public databases.
> "An algorithm for filtering molecular formulas is derived from seven heuristic rules..." (sources: src_036, src_034)

## Chemical Set Enrichment Statistics
A statistical method for finding biological meaning in untargeted metabolomics without the pitfalls of pathway mapping. Define sets of metabolites based on chemical structures/substructures rather than biological pathways. Include all identified compounds, optionally label by source (exposome, microbial), and calculate statistical over-enrichment compared to the experimental background.
> "we use chemical set enrichment all identified compounds are included because they have a unique structure structures can be automatically classified by using substructures" (sources: src_013)

## Hierarchical Omics Integration
A sequential approach to multi-omics where metabolomics generates a functional hypothesis to guide targeted genomic screening.
1. Apply metabolomics to patient cohorts to identify functional metabolic differences.
2. Formulate a mechanistic hypothesis based on altered metabolites.
3. Screen for specific SNPs only within genes related to that targeted metabolic function.
4. Validate surviving SNPs in a secondary cohort.
> "it generates hypotheses that you then validate by screening for specific Snips and therefore overcome the curse of these high numbers of of data that you get from genomic sequencing" (sources: src_015)

## Four Directions of Metabolite Analysis
A classification system for choosing the appropriate scope and methodology when designing a metabolite study.
1. **Target analysis:** Hypothesis-driven quantification of pre-defined biomarkers.
2. **Metabolite profiling:** Studying select pathways or compound classes simultaneously.
3. **Metabolomics:** Unbiased detection and quantification of all metabolic signals, including unknowns.
4. **Metabolic fingerprinting:** Rapid, chromatography-free acquisition of physical spectra to cluster and classify samples.
> "Metabolite analysis can thus broadly be classified into four different directions:" (sources: src_042)

## Identifying In-Source Fragmentation
A method using retention time modeling to verify lipid annotations and rule out false positives.
1. Apply retention time modeling to the annotated lipid.
2. Compare the observed retention time with the predicted retention time.
3. If the retention time is wrong for that specific lipid structure, flag it as an in-source fragmentation.
> "If you have the wrong lipid and a wrong retention time then it is an in-source fragmentation" (sources: src_011)

## Two-Tiered Screening Strategy
A strategy for screening large cohorts of healthy individuals for disease risk stratifications.
1. Screen the large cohort using rapid, low-cost metabolic fingerprinting to get a primary measure of risk.
2. Take samples from individuals identified as "at-risk".
3. Analyze this subset a second time using high-resolution metabolomic techniques to verify classification and identify specific biochemical pathway changes.
> "Samples of individuals identified at risk could then get analyzed a second time by more time consuming metabolomic techniques in order to strengthen and verify the classification of the first screen..." (sources: src_042)
