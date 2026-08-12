# Layer 2.3 --- Domain Mapping

## Purpose

This stage converts the large collection of UniProt feature annotations
into a concise map of biologically meaningful protein regions.

The sequence gives residue order; UniProt feature annotations provide
information about where structural or functional regions occur within
that sequence.

## Workflow

1.  Retrieve the reviewed UniProt protein entry.
2.  Read its annotated features.
3.  Extract feature type, description, and residue start/end positions.
4.  Remove low-priority annotation types that are not needed for the
    present domain map.
5.  Retain major structural/functional features such as signal peptide,
    transmembrane region, domain, and region.
6.  Record the resulting residue ranges in a processed domain-annotation
    file.

## Why this matters

The domain map creates the bridge between sequence and biological
interpretation. Instead of treating the protein as one continuous
sequence, later analyses can ask whether conservation or variation is
concentrated in particular regions.

## What the Domains Do

Different regions of a receptor perform different steps in the
signalling process.

- **Extracellular domain:** interacts with the ligand and helps determine
  ligand recognition and receptor binding.
- **Cysteine-rich regions:** contribute to the structural organization of
  the extracellular receptor and its ligand-binding surface.
- **Transmembrane region:** anchors the receptor in the cell membrane and
  helps position receptors for clustering after ligand binding.
- **Intracellular death domain:** in death receptors such as DR4 and DR5,
  provides the signalling interface required for recruitment of
  intracellular signalling proteins such as FADD and formation of the
  DISC.

These regions therefore contribute to different stages of TRAIL-mediated
apoptosis:

**TRAIL binding → receptor clustering → DISC formation → caspase
activation → apoptosis**

A change in a particular region may therefore have a different
consequence depending on its structural and functional role.

## Important distinction
A UniProt `Region` or `Domain` annotation should not automatically be
treated as equivalent to a specific mechanistic functional domain. The
annotation description and biological context must be considered before
assigning a function.

## Interpretation
Domain mapping allows sequence-level observations to be connected to
the mechanism of apoptosis. It provides the structural context needed
to determine whether conserved or variable sequence positions occur in
regions involved in ligand recognition, membrane organization, or
intracellular death signalling.
