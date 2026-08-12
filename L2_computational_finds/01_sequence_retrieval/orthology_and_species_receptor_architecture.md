# Orthology and Species-Specific Receptor Architecture

## Observation

During sequence retrieval, it became clear that the TRAIL receptor system cannot automatically be treated as a simple one-to-one set of equivalent receptors across human and mouse.

The human TNFRSF10 receptor family contains:

* DR4 — TNFRSF10A
* DR5 — TNFRSF10B
* DcR1 — TNFRSF10C
* DcR2 — TNFRSF10D

However, the mouse receptor repertoire does not reproduce this family as four independent one-to-one equivalents.

The mouse TNFRSF10 family therefore requires explicit orthology consideration rather than assuming:

> **Human receptor name = equivalent mouse receptor name**

This represents an important biological observation rather than merely a data-retrieval problem.

## Initial Assumption
The initial computational assumption was that a human receptor such as:

> **TNFRSF10A / DR4**

could be directly matched to a mouse receptor with the corresponding name.

The sequence-retrieval process demonstrated that this assumption cannot simply be carried forward without examining the underlying orthological relationship.

## Working Hypothesis
> **Differences in the receptor repertoire between species may represent an evolutionary difference in how TRAIL-mediated signalling is organized, rather than simply representing missing sequence data.**

Therefore, the computational analysis should determine whether the relevant structural and functional characteristics of the receptor system are conserved even when receptor identity is not preserved as a simple one-to-one relationship.

## Why This Matters
The project is no longer asking only:

> **"Is this receptor sequence conserved between species?"**

It must also ask:

> **"Is the receptor architecture and function conserved despite differences in receptor orthology and receptor repertoire?"**


## Effect on Layer 2.2 — Sequence Alignment
The sequences can still be aligned computationally using MAFFT.

However, MAFFT only determines how sequences can be placed into aligned positions. It does not determine whether the proteins represent strict orthologs.

Therefore:

> **The alignment can be computationally valid while its biological interpretation depends on the orthological relationship between the sequences.**

## Effect on Layer 2.3 — Domain Mapping
Domain mapping must determine whether corresponding structural regions are present rather than assuming that equivalent receptor names automatically have equivalent domains.

The analysis can therefore compare:

* extracellular architecture;
* ligand-binding regions;
* transmembrane regions;
* intracellular signalling regions;
* death-domain architecture where applicable.

This allows the project to ask whether **structural organization is conserved even when receptor identity differs**.

## Effect on Layer 2.4 — Conservation Analysis
Conservation scores must be interpreted in the context of orthology.

A high or low conservation score does not, by itself, prove conservation or divergence of the same receptor across species if the compared proteins do not represent strict one-to-one orthologs.

Therefore, conservation analysis must distinguish between:

> **conservation within corresponding receptor lineages**

and

> **similarity between related but differently organized receptor members.**

## Effect on Layer 2.5 — Mutation Analysis
Sequence differences must also be interpreted according to the relationship between the proteins being compared.

A difference may represent:

* ordinary sequence variation between corresponding proteins;
* evolutionary divergence;
* or a difference between receptor members that do not have a strict one-to-one relationship.

Therefore, mutation analysis should not automatically classify every sequence difference as a mutation affecting the same receptor function.

## Connection to Version 2 Hypothesis

This observation will be carried forward into the Version 2 hypothesis.

The final hypothesis will examine whether:

> **TRAIL-mediated apoptotic regulation is constrained by conserved receptor architecture even when the receptor repertoire and one-to-one orthological relationships differ between species.**

The four-human : one-mouse stringent orthological relationship identified during the project will therefore be treated as an important evolutionary observation when interpreting the later computational findings.


