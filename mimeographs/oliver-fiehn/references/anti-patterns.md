# Anti-Patterns

Fiehn explicitly warns against these common pitfalls in metabolomics, data integration, and analytical chemistry.

## Mapping Plasma Directly to Cellular Pathways
Assuming a metabolite in plasma reflects a specific cellular or mitochondrial pathway. Plasma is a transport system. Metabolites in plasma come from diet, microbes, and various organs, making direct mapping to specific cellular organelles highly inaccurate. (sources: src_013, src_015)

## Relying Exclusively on MS/MS
Depending solely on tandem mass spectrometry for metabolite annotation in large-scale analyses while ignoring retention time. It lacks the additional orthogonal data provided by retention time prediction, which is necessary for robust large-scale analysis and filtering out false positives. (sources: src_011, src_022)

## Unstructured Multi-Omics Integration
Throwing all multi-omics data together at once to "see what happens". It lacks structure and hypothesis generation, leading to messy, uninterpretable "hairball" networks rather than clear mechanistic insights.
> "not just you know giving like oh you know I just threw it all together and see what happens you know that's not a good idea" (sources: src_013, src_015)

## Using Pathway Set Enrichment
Relying on pathway set enrichment for metabolomics data. Pathway databases are sparse, poorly cover lipids, and cause double-counting of ubiquitous metabolites (like ATP or NADH), leading to skewed results. (sources: src_013)

## Ignoring Unknown Peaks
Relying solely on classical hypothesis-driven target analysis and ignoring statistically significant but unidentified metabolic peaks. This oversimplifies complex research problems, makes it hard to distinguish causal effects from simple associations, and completely misses unexpected metabolic responses. (sources: src_035, src_042)

## Hiding Data Until Publication
The "Classic" workflow of keeping data private until a paper is published, which prevents the community from finding and correcting misannotations. Researchers publish their findings and only later upload data to repositories, often leaving out crucial details. This makes the data not exactly findable or reusable, slowing down scientific progress. (sources: src_011)

## Ignoring Chemical Heuristics in Mass Spec
Relying solely on accurate mass measurements without applying chemical heuristic rules or isotopic pattern filtering. It leaves thousands of mathematically possible but chemically incorrect or highly unlikely candidate structures, making accurate structure elucidation impossible. (sources: src_034)

## Over-Annotating Lipid Structures
Claiming highly specific structural details (like exact regio isomers or double bond positions) without sufficient analytical evidence. Standard lipidomics usually lacks the time or specialized techniques to determine these exact positions, making highly specific structural claims dubious. (sources: src_011)

## Predicting Specificity from Sequence Homology
Predicting enzyme specificity purely from genome mapping and sequence homology. Single point mutations can drastically alter the output of metabolism, meaning high sequence similarity does not guarantee identical enzymatic function.
> "The idea that an enzyme specificity can be discerned just by blasting and mapping the genome is just horribly wrong." (sources: src_015)

## Similarity Alignments for Retention Time
Using complete similarity alignments for retention time instead of internal standards. It is highly susceptible to matrix effects and makes it nearly impossible to accurately compare data across different biological matrices like urine, stool, and plasma. (sources: src_012)
