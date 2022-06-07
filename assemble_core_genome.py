import sys
import os
from Bio import SeqIO

# Takes arguments input_directory, for directory containing aligned synteny block FNA files, and
# output_directory, for outputting combined core genome files

# Handle command line arguments
if len(sys.argv) != 3:
    print("Error: Two command line arguments are required.")
    sys.exit()
input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Dictionary with accession codes as keys, sequence strings as values
core_genomes = {}

# Read synteny block files (because the order of the files' names is arbitrary, it does not matter to traverse them
# in any order)
print_counter = 0
for fna_file in sorted(os.listdir(input_directory)):
    # Print progress
    print("%d\t%s" % (print_counter, fna_file))
    print_counter += 1
    # Iterate through appearances within each block's FNA file
    for record in SeqIO.parse(input_directory + fna_file, "fasta"):
        if record.id not in core_genomes:
            core_genomes[record.id] = str(record.seq)
        else:
            core_genomes[record.id] += str(record.seq)

# Write core genomes from core_genomes
print_counter = 0
for accession_code in core_genomes:
    # Print progress
    print("%d\t%s" % (print_counter, accession_code))
    print_counter += 1

    with open("%score_%s" % (output_directory, accession_code), "w+") as f:
        f.write(">%s\n" % accession_code)
        index = 0
        while index < len(core_genomes[accession_code]) - 60:
            f.write(core_genomes[accession_code][index:index+60] + "\n")
            index += 60
        f.write(core_genomes[accession_code][index:])
