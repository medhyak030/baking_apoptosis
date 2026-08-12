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

### Question
Can the TRAIL receptor family be treated as a one-to-one equivalent set of receptors across human, chimpanzee, and mouse?

### Working Hypothesis

The TRAIL receptor family should not automatically be assumed to have a perfect one-to-one correspondence across species. Human and chimpanzee receptor identities can be compared using established orthological relationships, whereas the mouse TNFRSF10 receptor repertoire requires explicit orthology consideration.

Therefore, receptor names or similar family membership alone should not be treated as sufficient evidence that two sequences represent the same evolutionary receptor.

### Interpretation

The sequence-retrieval stage therefore does more than obtain FASTA sequences. It establishes the biological identity of each sequence before it is used in downstream comparisons.

MGI's vertebrate homology framework distinguishes stringent one-to-one orthology from more complex homology relationships, making orthology an explicit consideration rather than an assumption.

This is particularly important for the TNFRSF10 family because the human TRAIL receptor system contains DR4/TNFRSF10A, DR5/TNFRSF10B, DcR1/TNFRSF10C, and DcR2/TNFRSF10D, while receptor repertoire and nomenclature differ between species.
