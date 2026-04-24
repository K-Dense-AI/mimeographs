# Heuristics and Rules of Thumb

Fiehn relies on these practical rules of thumb to troubleshoot instruments, filter data, and guide statistical analysis in metabolomics.

## The 80% Injector Rule
When GC-MS data quality fails, the primary suspect is almost always the injection system. Rather than the column or detector, issues like dirty liners or corroded syringes are responsible for 80% of poor quality results. (sources: src_051)

## Fold Change Over P-Values
Prioritize fold change over raw statistical significance, as significance just means "worthy of a second look."
> "it is the full change that i like the best because significance just means worthy a second look" (sources: src_013)

## No MS/MS, No Peak
A peak is only considered valid if it has an accompanying MS/MS spectrum. Relying solely on MS1 ions is insufficient for accurate compound qualification.
> "Just MS1 ions are not going into LC-BinBase because without an MS/MS you cannot qualify these compounds anyway." (sources: src_012)

## In-Source Fragmentation Check
If a lipid has the wrong retention time for its annotated structure, it is an in-source fragmentation.
> "If you have the wrong lipid and a wrong retention time then it is an in-source fragmentation" (sources: src_011)

## Guide the Statisticians
Do not leave statistics solely to statisticians; guide them to avoid overly strict diagnostic thresholds in mechanistic studies.
> "do not leave statistics to the statisticians engage with them and the reason is statistics is a science a field of science with lots of options" (sources: src_013)

## The 80% Detection Rule
Report peaks that are confidently detected in at least 80% of the samples of at least one study design group.
> "Recommended is to report peaks that are confidently detected in at least 80% of the samples of at least one study design group." (sources: src_051)

## Replicates Over Minimums
More replicates and repeats are always better than relying on the absolute minimum number of independent samples.
> "Researchers should also follow the general rule of statistics, that more replicates and repeats are better than relying on the absolute minimum number of independent samples..." (sources: src_042)

## Protein Reconstitution Rule
When drying down and reconstituting an extract, the protein fraction usually won't reconstitute, whereas metabolites and lipids will. (sources: src_011)
