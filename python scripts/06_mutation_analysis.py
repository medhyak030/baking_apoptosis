import os
import csv

alignment_dir = "data/processed/alignments"
conservation_dir = "data/processed/conservation"
output_dir = "data/processed/mutation_analysis"

os.makedirs(output_dir, exist_ok=True)

receptors = [
    "DR4",
    "DR5",
    "DCR1",
    "DCR2",
    "OPG"
]


def read_fasta(filename):

    names = []
    sequences = []

    with open(filename, "r") as file:

        sequence = ""

        for line in file:

            line = line.strip()

            if line.startswith(">"):

                if sequence:
                    sequences.append(sequence)
                    sequence = ""

                names.append(line[1:])

            else:
                sequence += line

        if sequence:
            sequences.append(sequence)

    return names, sequences


for receptor in receptors:

    alignment_file = os.path.join(
        alignment_dir,
        f"{receptor}_aligned.fasta"
    )

    conservation_file = os.path.join(
        conservation_dir,
        f"{receptor}_conservation.csv"
    )

    if not os.path.exists(alignment_file):
        print(f"Missing alignment: {alignment_file}")
        continue

    if not os.path.exists(conservation_file):
        print(f"Missing conservation file: {conservation_file}")
        continue

    names, sequences = read_fasta(alignment_file)

    with open(conservation_file, "r") as file:
        conservation_data = {
            int(row["Position"]): row
            for row in csv.DictReader(file) # Read conservation data from CSV
        }

    output_file = os.path.join( # Create output file path
        output_dir,
        f"{receptor}_variation.csv"
    )

    with open(output_file, "w") as output:

        output.write(
            "Position,Consensus,Conservation_Score,Residues,Variation\n"
        )

        for position in range(len(sequences[0])):

            residues = [
                sequence[position]
                for sequence in sequences
            ]

            non_gap_residues = [
                residue
                for residue in residues
                if residue != "-"
            ]

            if len(set(non_gap_residues)) <= 1:
                continue

            conservation = conservation_data.get(position + 1)

            consensus = (
                conservation["Consensus"]
                if conservation
                else ""
            )

            score = (
                conservation["Conservation_Score"]
                if conservation
                else ""
            )

            residue_string = "".join(residues)

            output.write(
                f"{position + 1},"
                f"{consensus},"
                f"{score},"
                f"{residue_string},"
                f"YES\n"
            )

    print(f"{receptor}: variation analysis saved")