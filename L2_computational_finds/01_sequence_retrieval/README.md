# Layer 2.1 --- Sequence Retrieval

## Purpose

This stage establishes the sequence dataset used for the computational
analysis of the TRAIL receptor family.

The project focuses on DR4 (TNFRSF10A), DR5 (TNFRSF10B), DcR1
(TNFRSF10C), DcR2 (TNFRSF10D), and OPG (TNFRSF11B).

## Workflow

1.  Read receptor/species metadata from `data/metadata/proteins.csv`.
2.  Construct a UniProt search query from gene and taxon information.
3.  Query the UniProt REST API.
4.  Check that the request succeeded.
5.  Examine returned entries and prefer a reviewed entry when
    appropriate.
6.  Record the accession.
7.  Download the corresponding FASTA sequence into
    `data/raw/<species>/`.

## Output

The raw FASTA files are the sequence inputs for later computational
stages. Raw sequences are kept separate from processed alignments and
annotations.

## Important limitation

The receptor family should not automatically be treated as perfectly
one-to-one across species. In particular, the mouse TNFRSF10 family
requires explicit orthology consideration rather than assuming that
every human receptor has an equivalent mouse receptor.

This limitation will be retained as a scientific consideration for the
final hypothesis.

## Current status

Sequence retrieval and FASTA downloading have been completed before the
conservation-score stage.

