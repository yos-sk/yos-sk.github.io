---
layout: about
title: About
permalink: /

profile:
  align: right
  image: prof_pic_v2.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>Staff scientist</p>
    <p><a href='https://www.ncc.go.jp/en/ri/division/genome_analysis_platform_development/index.html'>Division of Genome Analysis Platform Development</a> </p>
    <p>National Cancer Center Research Institute</p>
    <p>5-1-1 Tsukiji, Chuo-ku</p>
    <p>Tokyo 104-0045, Japan</p>

selected_papers: false # the "Selected papers" list is rendered at the end of the body below
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<!-- TODO: adjust your position/title and background below -->

I am a staff scientist in cancer genomics in the [Division of Genome Analysis Platform Development](https://www.ncc.go.jp/en/ri/division/genome_analysis_platform_development/index.html) at National Cancer Center Research Institute.
My research focuses on **cancer (epi)genome analysis using long-read sequencing**, with the goal of understanding the full spectrum of
genomic alterations in cancer, including those hidden in regions that are difficult to resolve with short reads. Please feel free to contact me by [e-mail](mailto:yosakam2@ncc.go.jp).

### Research interests

- **Haplotype-resolved cancer genomics**: personalized reference genomes built from long reads, enabling allele-aware analysis
  of somatic mutations, structural variants, and epigenetic changes ([PRCGAP](https://github.com/yos-sk/PRCGAP)).
- **Structural variants and phasing**: detection and characterization of complex rearrangements in lung cancer and other tumors
  using nanopore sequencing.
- **Long-read epigenomics**: whole-genome methylation profiling with enzymatic base conversion and nanopore sequencing
  ([nanoEM](https://github.com/yos-sk/nanoEM)).
- **Complex genomic regions**: centromeres and other repetitive regions in human diversity and cancer.

### Background

<!-- TODO: e.g. "I received my Ph.D. from ... under the supervision of ..." -->

More details are on the [research](/research/) and [papers](/publications/) pages, and the code is on [GitHub](https://github.com/yos-sk).

<h2>
  <a href="{{ '/publications/' | relative_url }}" style="color: inherit">Selected papers</a>
</h2>
{% include selected_papers.liquid %}
