import sys
import os
from Bio import SeqIO

# Run from SibeliaZ output folder with directory "blocks" created
# Constructs FNA files for non-repetitive synteny blocks with span above the threshold given as a command line argument
# MAFFT should applied to the output files of this script in order to align each synteny block before core genome
# construction

# Instantiations of this class represent synteny blocks
class Block:
    def __init__(self, lines, threshold):
        self.lines = []
        for i in lines:
            self.lines.append(i)
        self.nonunique_span = len(self.lines)

        # Get whether this block is sufficient, i.e. it is non-repetitive and has spane greater than or equal to the
        # threshold
        if self.nonunique_span < threshold:
            self.is_sufficient = False
            return
        accession_codes = []
        for line in self.lines:
            accession_code = line.split()[0]
            if accession_code in accession_codes:
                self.is_sufficient = False
                return
            accession_codes.append(accession_code)
        self.is_sufficient = True


# Handle command line argument to set threshold
if len(sys.argv) < 2:
    print("Error: At least one command line argument is required.")
    sys.exit()
if not sys.argv[1].isnumeric():
    print("Error: Integer argument not provided.")
    sys.exit()
threshold = int(sys.argv[1])

# Read genome files and store them in dictionary with file names as keys
fna_files = {}
print_counter = 0
for fna_file in os.listdir("../fnas/"):
    print(print_counter)
    print_counter += 1
    record = SeqIO.read("../fnas/" + fna_file, "fasta")
    fna_files[fna_file] = str(record.seq)

print("Done reading in FNA files.")

# Read SibeliaZ output file blocks_coords.gff
with open("blocks_coords.gff", "r") as f:
    # Skip reading file header
    for i in range(4):
        line = f.readline()
    # Setup
    seq_id = line.split()[8]
    blocks = []
    block_lines = []

    # Read through lines of blocks_coords.gff
    while line:
        block_lines.append(line)
        line = f.readline()
        if not line:
            blocks.append(Block(block_lines, threshold))
            block_lines.clear()
            break
        if line.split()[8] != seq_id:
            seq_id = line.split()[8]
            blocks.append(Block(block_lines, threshold))
            block_lines.clear()

print("Done reading blocks_coords.txt.")

# Iterate through list of Block objects, blocks, in order to write each block's FNA file
block_counter = 0
for block in blocks:
    # Checks whether the current block is non-repetitive and has sufficient span
    if block.is_sufficient:
        print(block_counter)
        # If so, open new file to write into
        with open("blocks/%d.fna" % block_counter, "w+") as f:
            for line in block.lines:
                words = line.split()
                fna_file = words[0] + ".fna"
                start = int(words[3])
                end = int(words[4])
                strand = words[6]
                f.write(">%s,%d\n" % (fna_file, start))
                appearance = fna_files[fna_file][start:end]
                # Handle leading vs. lagging strand
                if strand == "+":
                    f.write(appearance + "\n")
                elif strand == "-":
                    f.write(appearance[::-1] + "\n")

        block_counter += 1

