import os
from collections import Counter #collections is a built-in Python module that provides alternatives to Python's general-purpose built-in containers, such as dict, list, set, and tuple. It includes useful data structures like namedtuple(), deque, Counter, OrderedDict, defaultdict, and ChainMap. counter is a subclass of dict that helps count hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. It is part of the collections module in Python.

alignment_dir = "data/processed/alignments"
output_dir = "data/processed/conservation"

os.makedirs(output_dir, exist_ok=True) #os.makedirs() is a function in the os module that creates a directory recursively. If the directory already exists, it does not raise an error. The exist_ok=True parameter allows the function to ignore the error if the directory already exists.

receptors = [ #take all the receptors in the list and store them in a variable called receptors
    "DR4",
    "DR5",
    "DCR1",
    "DCR2",
    "OPG"
]


def read_fasta(filename): #define a function called read_fasta that takes a filename as an argument. This function reads a FASTA file and returns a list of sequences.
    sequences = [] #store the sequences in a list called sequences

    with open(filename, "r") as file:
        sequence = "" #sequence is a string that will store the current sequence being read from the FASTA file

        for line in file:
            line = line.strip() #look at each line in the file, remove any leading or trailing whitespace, and check if it starts with a ">" character. If it does, it indicates the start of a new sequence. If there is already a sequence being built, it is added to the list of sequences, and the current sequence string is reset. If the line does not start with ">", it is part of the current sequence and is appended to the sequence string.

            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
            else:
                sequence += line #confirm that the line is part of the current sequence and append it to the sequence string.

        if sequence:
            sequences.append(sequence)

    return sequences #appends the last sequence to the list of sequences and returns the list of sequences.


for receptor in receptors: #receptors is a list of receptor names. The for loop iterates over each receptor in the list and performs the following steps for each receptor.

    alignment_file = os.path.join(
        alignment_dir,
        f"{receptor}_aligned.fasta" #creates the path to the alignment file for the current receptor by joining the alignment directory and the receptor name with the suffix "_aligned.fasta"
    )

    if not os.path.exists(alignment_file):
        print(f"Missing alignment: {alignment_file}") #print a message indicating that the alignment file is missing
        continue

    sequences = read_fasta(alignment_file)

    if len(sequences) < 2: #cuz we have three sequences, we need at least two sequences to calculate conservation. If there are fewer than two sequences, it prints a message indicating that there are not enough sequences for the current receptor and continues to the next receptor in the loop.
        print(f"Not enough sequences for {receptor}")
        continue

    alignment_length = len(sequences[0]) #alignment_length is the length of the first sequence in the list of sequences. It assumes that all sequences in the alignment have the same length.

    output_file = os.path.join(
        output_dir,
        f"{receptor}_conservation.csv" #conservation file for the current receptor by joining the output directory and the receptor name with the suffix "_conservation.csv"
    )

    with open(output_file, "w") as output: #in write mode, which means that if the file already exists, it will be overwritten. If the file does not exist, it will be created. The output variable is a file object that can be used to write data to the file.

        output.write(
            "Position,Consensus,Conservation_Score,Residues\n"
        )

        for position in range(alignment_length): #iterates over each position in the alignment, from 0 to alignment_length - 1. For each position, it performs the following steps:

            column = [
                sequence[position] #position is the index of the current position in the alignment. It creates a list called column that contains the residues (amino acids or nucleotides) at the current position for all sequences in the alignment. It does this by accessing the character at the current position in each sequence.
                for sequence in sequences
            ]

            residues = [
                residue
                for residue in column
                if residue != "-"#cuz we need non gap residues to calculate conservation. It creates a list called residues that contains only the non-gap residues from the column list. It does this by filtering out any residues that are equal to the gap character "-".
            ]

            if not residues:
                continue #green signal that there are no non-gap residues at the current position, so it skips to the next position in the loop.

            counts = Counter(residues) #counts is a Counter object that contains the frequency of each residue in the residues list.

            consensus, count = counts.most_common(1)[0] #consensus is the residue with the highest frequency (the most common residue) at the current position, and count is the number of times that residue appears in the residues list. It does this by calling the most_common(1) method on the counts object, which returns a list of tuples containing the most common residue and its count. The [0] index is used to access the first tuple in the list.

            score = count / len(residues) #score formula is the conservation score for the current position, calculated as the count of the consensus residue divided by the total number of non-gap residues at that position. It represents the proportion of sequences that have the consensus residue at that position.

            output.write( #writes a line to the output file for the current position, containing the position (1-based index), consensus residue, conservation score (formatted to two decimal places), and the residues at that position (joined into a single string). It uses an f-string to format the output line.
                f"{position + 1},"
                f"{consensus},"
                f"{score:.2f},"
                f"{''.join(column)}\n"
            )

    print(f"{receptor}: conservation saved")