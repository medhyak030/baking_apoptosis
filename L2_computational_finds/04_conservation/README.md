# Layer 2.4 --- Conservation Analysis

## Purpose

This stage will quantify how strongly sequence positions are conserved
across the aligned species.

The biological question is not simply whether two sequences are similar.
It is whether particular receptor regions show stronger evolutionary
constraint than others.

## Input

The receptor-specific aligned FASTA files from Layer 2.2 will be used
together with the domain/region coordinates from Layer 2.3.

## Planned analysis

1.  Read each multiple sequence alignment.
2.  Examine aligned columns.
3.  Calculate a conservation measure for relevant positions or regions.
4.  Compare conservation across annotated regions.
5.  Relate conserved and variable regions to protein architecture.

## Interpretation framework

High conservation can indicate evolutionary constraint, but conservation
alone does not prove a particular molecular function. Sequence
variability also does not automatically mean that a region is
biologically unimportant. Interpretation must use the domain map and
receptor architecture.

## Hypothesis connection

This stage will provide evidence for the later hypothesis concerning
whether functionally important receptor regions are more evolutionarily
constrained than regions that can tolerate sequence variation.

The final hypothesis will be written after the computational findings
are complete rather than assumed in advance.

## Current status

The theoretical framework is defined, but **conservation scores have not
yet been calculated**. No conservation result is recorded here.
