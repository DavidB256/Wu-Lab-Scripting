import sys
import os
from Bio import SeqIO

# Run from SibeliaZ output folder with containing blocks_coords.gff and sequence FNA files in folder called fnas in
# parent directory
# Two command line arguments are threshold and output_dir, respectively (output_dir must be given with a slash at end)
# Constructs FNA files for non-repetitive synteny blocks with span above given threshold
# MAFFT should applied to the output files of this script in order to align each synteny block before core genome
# construction

# Instantiations of this class represent synteny blocks
class Block:
    def __init__(self, lines, threshold):
        self.lines = []
        for i in lines:
            self.lines.append(i)
        self.nonunique_span = len(self.lines)

        # Get whether this block is sufficient, i.e. it is non-repetitive and has span greater than or equal to the
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
if len(sys.argv) < 3:
    print("Error: At least two command line arguments are required.")
    sys.exit()
threshold = int(sys.argv[1])
output_dir = sys.argv[2]

# Read genome files and store them in dictionary with file names as keys and SeqIO sequences as values in fna_files
fna_files = {}
print_counter = 0
for fna_file in os.listdir("../fnas/"):
    # Progress counter
    print(print_counter)
    print_counter += 1
    # Add new genome file into fna_files with file name as key and SeqIO sequence as value
    record = SeqIO.read("../fnas/" + fna_file, "fasta")
    fna_files[fna_file] = record.seq

print("Done reading in FNA files.")

# Read SibeliaZ output file blocks_coords.gff
with open("blocks_coords.gff", "r") as f:
    # Skip reading file header
    for i in range(4):
        line = f.readline()
    # Setup
    seq_id = line.split()[8]
    # blocks is a list of Block objects
    blocks = []
    # block_lines is a list of lines corresponding to each synteny block that gets cleared after reading each block
    block_lines = []

    # Read through lines of blocks_coords.gff
    while line:
        block_lines.append(line)
        line = f.readline()
        # Handle reaching end of blocks_coords.gff
        if not line:
            blocks.append(Block(block_lines, threshold))
            block_lines.clear()
            break
        # Handle reaching new synteny block, as indicated by new sequence ID in ninth column
        if line.split()[8] != seq_id:
            seq_id = line.split()[8]
            blocks.append(Block(block_lines, threshold))
            block_lines.clear()

print("Done reading blocks_coords.txt.")

# Iterate through blocks, the list of Block objects, in order to write each block's FNA file into output_dir
block_counter = 0
for block in blocks:
    # Checks whether the current block is non-repetitive and has sufficient span
    if block.is_sufficient:
        # Print progress
        print(block_counter)
        # Open new FNA file in output_dir
        with open("%s%d.fna" % (output_dir, block_counter), "w+") as f:
            for line in block.lines:
                words = line.split()
                fna_file = words[0] + ".fna"
                start = int(words[3])
                end = int(words[4])
                strand = words[6]
                f.write(">%s\n" % fna_file)
                appearance = fna_files[fna_file][start:end]
                # Handle leading vs. lagging strand
                if strand == "+":
                    f.write(str(appearance) + "\n")
                elif strand == "-":
                    f.write(str(appearance.reverse_complement()) + "\n")

        block_counter += 1
