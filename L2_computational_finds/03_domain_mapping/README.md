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

## Important distinction

A UniProt `Region` or `Domain` annotation should not automatically be
treated as equivalent to a specific mechanistic functional domain. The
annotation description and biological context must be considered before
assigning a function.

## Current status

Domain/feature retrieval and positional extraction have been completed.
The next step after documentation is quantitative conservation analysis,
so this README does not claim conservation results.
