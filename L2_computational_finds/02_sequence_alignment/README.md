# Layer 2.2 --- Sequence Alignment

## Purpose

This stage compares the retrieved protein sequences across the selected
species using multiple sequence alignment (MSA).

The immediate goal is to place comparable sequence positions into
alignment columns so that later conservation and variation analyses can
be performed.

## Workflow

1.  Collect the available FASTA sequence for each receptor.
2.  Combine the species sequences into a receptor-specific input FASTA.
3.  Run MAFFT on each receptor-specific input.
4.  Save the resulting aligned FASTA in `data/processed/alignments/`.

Each receptor has its own alignment rather than combining unrelated
receptors.

## Interpretation

MAFFT provides the positional framework for comparing the retrieved sequences, but the biological meaning of that comparison depends on their orthological relationship.

- Identical residues indicate matching amino acids at an aligned position.
- Substitutions indicate sequence differences between the compared proteins.
- Gaps (`-`) indicate alignment insertions or deletions.
- Conserved regions provide candidates for evolutionary constraint, but require quantitative analysis in 2.4.

Thus, the alignment establishes **where sequences correspond**, while the subsequent analyses determine **what those correspondences mean biologically**.

## Current status
The alignment workflow has been corrected so that all five receptor
inputs are processed when the corresponding FASTA files exist.

Intended outputs: - `DR4_aligned.fasta` - `DR5_aligned.fasta` -
`DCR1_aligned.fasta` - `DCR2_aligned.fasta` - `OPG_aligned.fasta`
