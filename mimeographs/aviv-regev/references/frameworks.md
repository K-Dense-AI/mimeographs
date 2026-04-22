# Frameworks

This document details the step-by-step frameworks Aviv Regev uses to structure research, validate discoveries, and integrate AI into scientific workflows.

## Lab in a Loop

**Canonical statement:** An iterative operational model for AI-driven drug discovery that integrates experiments, data, and algorithms.

**Rationale:** The space of genetic and therapeutic possibilities is too vast to explore empirically. By closing the loop between AI predictions and automated lab experiments, the system continuously learns and navigates the vast therapeutic space efficiently.

**Steps:**
1. Use experimental or clinical data to train computational models.
2. Use the trained models to predict the next set of experiments to run.
3. Iterate the process at scale to yield specific project predictions and globally improve the model.

> "...scientists use experimental or clinical data to train models, the models are used to predict the next set of experiments, and the process is iterated, at scale..."
*(sources: src_010)*

## Computational Modeling of Cellular Circuits

**Canonical statement:** A method for deciphering how cellular networks and protein signals change in response to stimuli.

**Rationale:** Cells function like complex computers. To understand their "wiring diagrams" in health and disease, we must perturb them and computationally model the resulting cascade of molecular events.

**Steps:**
1. Gather dynamic gene expression data using single-cell RNA sequencing.
2. Subject cells to stimuli (hormones, pathogens).
3. Create algorithms to decipher the most likely sequence of molecular events.
4. Test predictions by silencing specific genes (e.g., via CRISPR) and observing the response.

> "the modeling step"
*(sources: src_021)*

## Cellular Atlas Dimensions

**Canonical statement:** The required dimensions for building a comprehensive reference map of biological tissues.

**Rationale:** A true atlas cannot just be a flat list of parts. It must capture the multidimensional nature of cells, including their types, states, locations, and developmental histories.

**Steps:**
1. Catalog all distinct cell types.
2. Distinguish between different states for the same cell type.
3. Position all cells in 3D spatial locations.
4. Identify salient features during dynamic transitions.
5. Trace the entire developmental lineage.

> "Well, obviously the first thing that should be there is the listing of all of the different cell types... We also want to be able to distinguish between different states... position all of these cells in their three dimensional locations..."
*(sources: src_031)*

## Molecular-Morphological Validation Framework

**Canonical statement:** A process for discovering and validating new cell types using unsupervised single-cell RNA-seq clustering.

**Rationale:** Computational predictions of new cell types must be grounded in physical reality. This framework bridges the gap between abstract algorithmic clusters and observable tissue morphology.

**Steps:**
1. Perform unsupervised clustering on single-cell RNA-seq data.
2. Identify differentially expressed marker genes for each cluster.
3. Use double-color FISH to confirm co-expression with known markers.
4. If no markers exist, use sparse morphological labeling combined with FISH to match the new molecular marker to expected morphology.

> "we took each of the Clusters we predicted molecular markers... and now we're going to see whether the marker is actually expressed in the appropriate type"
*(sources: src_013)*
