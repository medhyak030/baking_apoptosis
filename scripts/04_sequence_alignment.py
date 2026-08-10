import os
import subprocess

receptors = {
    "DR4": "TNFRSF10A",
    "DR5": "TNFRSF10B",
    "DCR1": "TNFRSF10C",
    "DCR2": "TNFRSF10D",
    "OPG": "TNFRSF11B"
}

species = {
    "Homo_sapiens": "",
    "Mus_musculus": "",
    "Pan_troglodytes": ""
}

output_dir = "data/processed/alignments"
os.makedirs(output_dir, exist_ok=True)

for protein_name, gene in receptors.items():

    combined_file = os.path.join( #selects the combined file path
        output_dir,
        f"{protein_name}_input.fasta"
    )

    alignment_file = os.path.join( #selects the alignment file path
        output_dir,
        f"{protein_name}_aligned.fasta"
    )

    with open(combined_file, "w") as output:

            for species_name in species:

                fasta_file = f"data/raw/{species_name}/{gene}.fasta"

                if not os.path.exists(fasta_file):
                    print(f"Missing FASTA: {fasta_file}")
                    continue

                with open(fasta_file, "r") as input_file:
                    sequence = input_file.read()

                output.write(sequence)

    print(f"Created input: {combined_file}")

    with open(alignment_file,"w") as output:
        subprocess.run( #calls out external program mafft to run MSA
            ["mafft", "--auto", combined_file], #runs MAFFT alignment, auto choses appropriate alignment strategy based on input size and complexity
            stdout=output #opens the alignment file for writing
        )

    print(f"Alignment saved: {alignment_file}")