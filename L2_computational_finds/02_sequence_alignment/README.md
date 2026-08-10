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

An aligned FASTA is not yet a conservation score. It is the positional
framework from which conservation can later be calculated.

-   Identical residues can occupy the same column.
-   Substitutions show sequence differences between species.
-   Gaps (`-`) represent alignment insertions/deletions.
-   Conserved blocks can suggest sequence constraint, but quantitative
    conservation must be calculated separately.

## Current status

The alignment workflow has been corrected so that all five receptor
inputs are processed when the corresponding FASTA files exist.

Intended outputs: - `DR4_aligned.fasta` - `DR5_aligned.fasta` -
`DCR1_aligned.fasta` - `DCR2_aligned.fasta` - `OPG_aligned.fasta`

No conservation score has been calculated yet.
