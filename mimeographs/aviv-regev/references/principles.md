# Core Principles

This document outlines the foundational principles and decision rules that drive Aviv Regev's approach to computational biology and scientific discovery.

## Computation Before Collection

**Canonical statement:** Computation must be integrated into experimental design before data collection, not just treated as a post-experiment analysis step.

**Rationale:** Statistical frameworks and power analyses are necessary to make decisions throughout every step of the process. If you wait until after the data is collected to involve computation, you miss the opportunity to ensure the right number of cells and spatial patterns are captured in the first place.

> "computation for the human cell Atlas is not just about what happens after the data has been collected it is as ever it is at every point and in particular before the data has been collected and the experiment has been designed"
*(sources: src_020)*

## Standardized Consortium Approach

**Canonical statement:** Comprehensive biological understanding requires a coordinated, standardized approach rather than isolated, bespoke experiments.

**Rationale:** When individual labs use their own uncoordinated techniques, they produce disconnected findings riddled with technical noise and batch effects. A unified, shared approach is necessary to build foundational biological catalogs that reflect true biological variation rather than differences in sample prep.

> "...only if we do it in a standardized way from sampling acquisition, to sample prep, to QC, to analytics would we ever have a chance of actually creating a meaningful catalog that is not riddled by noise. And our body didn’t hear that it actually belongs to different institutes."
*(sources: src_009, src_016, src_021, src_031)*

## Maximize Cell Numbers Over Depth

**Canonical statement:** In complex tissues, maximizing the number of cells analyzed is far more important than the sequencing depth per cell.

**Rationale:** To accurately cluster highly diverse populations and capture rare cell types, analyzing tens of thousands of cells shallowly is far more effective than analyzing a small number of cells deeply. Over-sequencing mostly yields duplicate reads and wastes resources.

> "large cell numbers are really critical when you have a complex tissue. the number of cells is probably the most the best thing you can do for yourself more so than the depth per cell"
*(sources: src_013)*

## Cells as the Genotype-Phenotype Bridge

**Canonical statement:** Cells are the critical intermediate between genetic variants and disease phenotypes.

**Rationale:** To functionally characterize genetic variants, understand how they cause disease, or perform effective gene therapy, we must know exactly which specific (and sometimes rare) cells those variants manifest in.

> "Now, cells are also a key intermediate in between the genotype and the phenotypes that we care about so dearly... if we actually want to functionally characterize variants and act upon them we have to know which cells we are dealing with."
*(sources: src_016, src_021, src_031)*

## Algorithm Dictates Insight

**Canonical statement:** The choice of algorithm dictates the biological insight you uncover from a dataset.

**Rationale:** Data does not speak for itself; the lens matters. Applying different mathematical and AI approaches to the exact same dataset reveals fundamentally different biological phenomena, from static cell types to dynamic differentiation patterns.

> "When algorithms cluster, we find cell types. When algorithms find continual trajectories or optimal transport maps, we see dynamical patterns, like cell differentiation, or tumorous cells."
*(sources: src_014)*

## Under-Sampled Inference

**Canonical statement:** Exhaustive measurement of complex biological systems is impossible; researchers must leverage under-sampled data and cartographic scaling.

**Rationale:** Because of the combinatorial explosion of variables in biology, we cannot measure every cell or genetic interaction. By applying principles of cartography and low-dimensional inference, we can extract comprehensive understanding from highly under-sampled data.

> "Overcoming this limitation is not simply a matter of reducing costs with existing approaches; for complex biological systems it will likely never be possible to comprehensively measure and perturb every combination of variables of interest."
*(sources: src_029, src_031)*

## AI for Noisy Biological Data

**Canonical statement:** Massive, noisy biological data requires AI algorithms to extract meaningful insights.

**Rationale:** Modern lab technologies produce data at an unprecedented scale but with high levels of noise. Manual or traditional analysis is insufficient; AI is the necessary cost to make sense of this complexity.

> "There’s no free lunch. You always have to pay. If we want to make sense of this noisy and messy data, we need AI algorithms"
*(sources: src_014)*

## Interdisciplinary Rigor

**Canonical statement:** Study interdisciplinary subjects at their maximum level of rigor.

**Rationale:** To effectively combine different disciplines, you must first understand them at their purest, most rigorous level (e.g., learning math from mathematicians) rather than settling for a watered-down version tailored for outsiders.

> "you actually had to study it at its maximum level... at which point it was easier for you to bring the disciplines together"
*(sources: src_019)*
