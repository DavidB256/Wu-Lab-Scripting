import sys
import os
from Bio import SeqIO

# Takes arguments input_directory, for directory containing aligned synteny block FNA files, and
# output_directory, for outputting combined core genome files


class CoreGenome:
    def __init__(self):
        # Keys are block start loci, values are sequences
        self.blocks_dict = {}

    def add(self, start_locus, sequence):
        self.blocks_dict[start_locus] = sequence

    def assemble_genome_string(self):
        genome_string = ""
        for block in self.blocks_dict:
            genome_string += str(self.blocks_dict[block])
        return genome_string

# Handle command line arguments
if len(sys.argv) != 3:
    print("Error: At least one command line argument is required.")
    sys.exit()
input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Keys are accession codes, values are CoreGenome objects
core_genomes_dict = {}

# Read synteny block files
print_counter = 0
for fna_file in os.listdir(input_directory):
    print("%d\t%s" % (print_counter, fna_file))
    print_counter += 1

    for record in SeqIO.parse(input_directory + fna_file, "fasta"):
        # Read in accession code and start locus from each FASTA header in the synteny block file
        fasta_header_words = str(record.id).split(",")
        accession_code = fasta_header_words[0]
        start_locus = int(fasta_header_words[1])

        if accession_code not in core_genomes_dict:
            core_genomes_dict[accession_code] = CoreGenome()
        core_genomes_dict[accession_code].add(start_locus, record.seq)

# Write core genomes
print_counter = 0
for accession_code in core_genomes_dict:
    print("%d\t%s" % (print_counter, accession_code))
    print_counter += 1

    with open("%score_%s" % (output_directory, accession_code), "w+") as f:
        f.write(">" + accession_code + "\n")

        genome_string = core_genomes_dict[accession_code].assemble_genome_string()
        index = 0
        while index < len(genome_string) - 60:
            f.write(genome_string[index:index+60] + "\n")
            index += 60
        f.write(genome_string[index:])

