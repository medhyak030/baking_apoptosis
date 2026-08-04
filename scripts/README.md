
### Purpose

This directory contains the computational components of the Baking_Apoptosis project.

Each script represents one reproducible stage of the computational pipeline and is designed to answer a specific biological question. Scripts are intentionally modular, with each performing a single well-defined task. This structure improves reproducibility, debugging, and future expansion of the project.

# Computational Pipeline

Stage 1 — Sequence Retrieval

Objective:
Retrieve the canonical protein sequences of the core TRAIL signalling components from UniProt.

Output:
Protein FASTA sequences stored in `data/raw/`.

Script:
`01_download_sequences.py`

---

Stage 2 — Sequence Validation

Objective:
Verify that the downloaded sequences correspond to the intended proteins.

Validation includes:

- Gene name
- Protein name
- UniProt accession
- Organism
- Sequence length
- Review status

Output:
Validated sequence dataset.

---

Stage 3 — Similarity Search (BLAST)

Objective:
Identify homologous protein sequences and verify sequence identity.

Output:

- BLAST reports
- Homolog identification
- Similarity statistics

---

Stage 4 — Multiple Sequence Alignment

Objective:
Compare orthologous protein sequences across selected species.

Species (Version 2):

- Homo sapiens
- Mus musculus
- Pan troglodytes

Output:

- Multiple sequence alignments
- Conserved residues
- Variable residues

---

Stage 5 — Functional Domain Mapping

Objective:
Map experimentally annotated functional domains onto aligned protein sequences.

Domains include:

- Cysteine-rich domains (CRDs)
- Stalk region
- Transmembrane region
- Death domain

Output:
Annotated domain maps.

---

Stage 6 — Evolutionary Conservation Analysis

Objective:
Evaluate sequence conservation across species and determine whether functionally important regions exhibit higher evolutionary conservation.

Output:

- Conservation profiles
- Conserved functional residues
- Comparative analyses

---

Stage 7 — Mutation Analysis

Objective:
Map experimentally reported mutations onto conserved protein regions and evaluate their potential relationship to receptor function.

Output:

- Mutation annotations
- Domain-specific mutation mapping
- Functional interpretation
