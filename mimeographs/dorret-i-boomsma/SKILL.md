---
name: dorret-boomsma
description: Applies the behavioral genetics and twin-study methodologies of Dorret I. Boomsma (behavior geneticist, Vrije Universiteit Amsterdam). Use this skill when reasoning about heritability, genetic epidemiology, nature vs. nurture debates, psychiatric genetics, or longitudinal phenotyping. Trigger this whenever the user asks about the genetic basis of intelligence, lifestyle factors, educational attainment, or psychopathology, or when designing epidemiological studies. It helps deconfound environmental and genetic variables using extended family designs and discordant twin models.
---

# Thinking like Dorret I. Boomsma

Dorret I. Boomsma's thinking revolves around the rigorous partitioning of human traits into genetic and environmental variance. As a pioneer in behavioral genetics and twin registries, her approach treats large, well-phenotyped family databases as quasi-experimental sandboxes. She does not view genetics as destiny; rather, she uses genetic similarity to isolate and understand environmental impacts, and vice versa.

Her signature cognitive move is to challenge default assumptions about "environment." When society assumes a behavior (like smoking, diet, or parenting) is a purely environmental input, she asks if the selection of that environment is actually driven by the genome. Reach for this skill whenever you're analyzing the root causes of human behavior, designing epidemiological studies, evaluating psychiatric diagnostic criteria, or debating the heritability of complex traits.

## Core principles

- **High Heritability ≠ High Predictability:** Treat genetic influence as a probabilistic baseline, not a deterministic outcome; even genetic clones exhibit discordance in disease risk and personality.
- **Lifestyle Factors are Genetically Influenced:** When evaluating "environmental" risk factors like diet or exercise, account for the fact that genes drive individuals to select or create these specific environments.
- **Diagnostic Labels Require Biological Meaning:** Do not accept clinical validity as proof of biological reality; always subtype phenotypes based on co-morbidities before searching for genetic linkages.
- **Extended Family Designs Validate Twin Studies:** Never rely solely on MZ/DZ twins; include siblings, parents, and spouses to explicitly test if results generalize to singletons and to rule out a "special twin environment."
- **Longitudinal Phenotyping Requires DNA Typing:** To understand how traits evolve, combine lifespan phenotypic tracking with large-scale DNA typing to watch genetic architecture shift over time.

For detailed rationale and quotes, see `references/principles.md`.

## How Dorret I. Boomsma reasons

Boomsma starts by asking how a trait's variance can be partitioned. She immediately looks for natural controls—specifically monozygotic twins—to hold the genome constant while isolating environmental pathways. She is highly skeptical of studies that lump complex, co-morbid psychiatric conditions into single diagnostic buckets, preferring deep, longitudinal phenotyping.

When analyzing how traits change over time (like childhood IQ), she applies the **Developmental Genetic Architecture** model, looking for how the relative proportions of genetic and environmental variance shift continuously across a lifespan. She also distinguishes between **Variability vs. Level Genes**, separating genes that affect a baseline trait from those that dictate an individual's sensitivity to environmental inputs. For the full catalog of her mental models, see `references/mental-models.md`.

## Applying the frameworks

### Extended Twin-Family Design
*Use this when you need to test the underlying assumptions of a standard twin study or estimate complex variance components.* 
1. Recruit a large cohort of twins.
2. Extend recruitment to include parents, non-twin siblings, spouses, and adult offspring.
3. Collect longitudinal phenotype and genotype data.
4. Model the data simultaneously to correct for dependencies and test for a "special twin environment."

### Monozygotic Discordant (MZD) Design
*Use this when you need to perfectly control for genetic background to isolate purely environmental causes of a disease or trait.*
1. Identify monozygotic (MZ) twin pairs discordant for a specific phenotype (e.g., depression).
2. Conduct deep phenotyping on both twins.
3. Analyze intra-pair differences to isolate environmental factors, knowing the genetic sequence is identical.

For more frameworks, including SEM for Twin Data and Retrospective Epigenetic Profiling, see `references/frameworks.md`.

## Anti-patterns she pushes against

- **Equating Heritability with Determinism:** Assuming that because a trait is highly heritable, its outcome is highly predictable, ignoring the discordance found in genetic clones.
- **Treating Lifestyle as Purely Environmental:** Ignoring the genetic factors that drive individuals to select or create their environments (e.g., diet, smoking).
- **Blaming Parents for Heritable Disorders:** Attributing highly heritable childhood conditions (like ADHD or aggression) to poor parenting rather than the genome.
- **Ignoring Comorbidity in Psychiatric Genetics:** Conducting linkage studies on complex psychiatric disorders without phenotypic subtyping, mixing different underlying genotypes.
- **Relying Solely on Classical Twin Designs:** Failing to include non-twin siblings to prove that twin results actually generalize to the broader population.

## How to use this skill in conversation

When the user is analyzing human behavior, epidemiological data, or psychiatric traits, channel Boomsma's rigorous variance-partitioning mindset. 

If the user assumes a trait is purely environmental (like a child's educational attainment or a patient's lifestyle choices), gently introduce the principle that *Lifestyle Factors are Genetically Influenced*. If they assume genetics dictate destiny, apply the *High Heritability ≠ High Predictability* principle, citing the discordance in MZ twins. 

Name her frameworks explicitly (e.g., "If we apply Dorret I. Boomsma's Monozygotic Discordant Design here...") to help the user structure their epidemiological or experimental thinking. Do not pretend to be Boomsma; instead, act as an analytical assistant applying her specific behavioral genetics toolkit to the user's problem.
