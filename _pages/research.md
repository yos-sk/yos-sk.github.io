---
layout: page
permalink: /research/
title: Research interests
description: Long-read sequencing approaches to understand cancer genomes in their full complexity.
nav: true
nav_order: 1
---

## Cancer genome analysis using long-read sequencing technologies

### Haplotype-resolved cancer genome analysis

Standard cancer genome analysis aligns reads to a single linear reference genome, which hides allele-specific information and
introduces reference bias. Using long reads, we phased somatic and germline variants to reveal the allelic architecture of
cancer genomes. Building on this, we develop **PRCGAP** (Personalized Reference genome-based Cancer Genome Analysis Pipeline),
which builds a diploid personalized reference genome from each patient's long reads and uses it to analyze somatic mutations,
structural variants, and DNA methylation in a haplotype-resolved manner.

- Sakamoto _et al._, _bioRxiv_ (2026). [doi:10.64898/2026.05.28.728591](https://doi.org/10.64898/2026.05.28.728591)
- Sakamoto _et al._, _Nature Communications_ (2022). [doi:10.1038/s41467-022-31133-6](https://doi.org/10.1038/s41467-022-31133-6)
- Code: [PRCGAP](https://github.com/yos-sk/PRCGAP)

### Structural variants in cancer genomes

Using nanopore long-read sequencing, we characterized structural variants in lung cancer genomes, including a class of
cancerous local amplifications that are difficult to resolve with short reads.

- Sakamoto _et al._, _Genome Research_ (2020). [doi:10.1101/gr.261941.120](https://doi.org/10.1101/gr.261941.120)
- Haga, Sakamoto _et al._, _Nature Communications_ (2023). [doi:10.1038/s41467-023-43732-y](https://doi.org/10.1038/s41467-023-43732-y)
- Reviews: _J Hum Genet_ (2020), _CSBJ_ (2021)

### Centromeres and complex regions

In collaboration, we study centromeric and other repetitive regions that become accessible with long reads and
telomere-to-telomere assemblies.

- Shiraishi _et al._, _Cell_ (2026). [doi:10.1016/j.cell.2026.08.053](https://doi.org/10.1016/j.cell.2026.08.053)
- Suzuki _et al._, _Bioinformatics_ (2026). [doi:10.1093/bioinformatics/btaf648](https://doi.org/10.1093/bioinformatics/btaf648)

## Long-read epigenomics

We developed **nanoEM**, which combines enzymatic base conversion with nanopore sequencing to obtain long-range,
whole-genome methylation patterns, and have applied long-read methylation analysis to clinical specimens.

- Sakamoto _et al._, _Nucleic Acids Research_ (2021). [doi:10.1093/nar/gkab397](https://doi.org/10.1093/nar/gkab397)
- Code: [nanoEM](https://github.com/yos-sk/nanoEM)
