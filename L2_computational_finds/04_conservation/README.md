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

### Question 1
Are the functionally important regions of TRAIL receptors more strongly conserved across species than regions that can tolerate greater sequence variation?

### Working Hypothesis
Functionally important regions of TRAIL receptors will show stronger evolutionary conservation because their structural integrity is required for receptor function. Regions with greater regulatory or structural flexibility may tolerate more sequence variation.

### What We Did
The MAFFT-aligned FASTA files were analysed position-by-position using Python.

For each alignment position:

- `Position` represents the alignment column.
- `Consensus` represents the most common non-gap amino acid.
- `Conservation_Score` represents the proportion of non-gap sequences containing the consensus residue.
- `Residues` records the actual residues, including gaps, present at that alignment position.

The conservation score was calculated using Python's `collections.Counter`.

For three sequences:

- `1.00` = all three sequences contain the same residue.
- `0.67` = two of three contain the same residue.
- `0.33` = the three non-gap residues are different.

### Interpretation Framework
High conservation can indicate evolutionary constraint, but conservation alone does not prove a particular molecular function. Similarly, sequence variability does not automatically mean that a region is biologically unimportant.

The conservation score therefore needs to be interpreted together with:

- the sequence alignment;
- the domain map from 2.3;
- the receptor architecture;
- the known role of the corresponding region.

The purpose is not simply to identify the highest numerical scores, but to determine **where conservation occurs and what biological function those regions may support**.

### Question 2 — Conservation and Apoptotic Function
How could evolutionary conservation of receptor regions help preserve the mechanism of TRAIL-mediated apoptosis, including ligand recognition, receptor recruitment and clustering, DISC formation, and downstream signalling?

### Working Hypothesis
Regions that are essential for the TRAIL apoptotic pathway should experience stronger evolutionary constraint because changes in these regions could interfere with the physical interactions required for receptor function.

If the ligand-binding region is conserved, this may help preserve TRAIL recognition. Conservation of membrane-associated regions may help maintain receptor positioning and clustering. Conservation of intracellular signalling regions, particularly the death domain of death receptors, may help preserve recruitment of signalling proteins and DISC formation.

Therefore, conservation may reflect the evolutionary preservation of the **sequence-level components required to maintain the apoptotic signalling process**.

### Interpretation
The conservation analysis allows us to move from:

**"Which amino acids are conserved?"**

to:

**"Which parts of the receptor mechanism are being conserved?"**

A pattern in which functionally important regions show stronger conservation would support the idea that evolutionary constraint helps preserve the molecular steps required for TRAIL-mediated apoptosis:

**TRAIL recognition → receptor recruitment/clustering → DISC formation → caspase activation → apoptosis**

However, this remains an interpretation of the conservation pattern. Conservation alone cannot establish that a particular residue causes or maintains a specific apoptotic function.

### Hypothesis Connection
This stage provides evidence for the hypothesis that functionally important receptor regions are more evolutionarily constrained than regions that can tolerate greater sequence variation.

The final hypothesis will be refined after the remaining computational analysis, particularly mutation analysis, rather than being assumed in advance.
