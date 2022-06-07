
import sys
import os
from Bio import SeqIO

# This script gets called by align_synteny_blocks.py after it creates grep_output.txt by extracting the FASTA headers
# from all associated FNA files

with open("blocks_coords.txt", "r") as f:
    # Construct dictionary matching sequence IDs to accession codes from blocks_coords.txt header
    seq_id_to_accession_code_dict = {}
    line = f.readline()
    line = f.readline()
    while line[0] != "-":
        seq_id = line.split()[0]
        accession_code = line.split()[2]
        seq_id_to_accession_code_dict[seq_id] = accession_code
        line = f.readline()

    print(1)

    num_of_seqs = len(seq_id_to_accession_code_dict)
    full_span_synteny_block_counter = 0

    # Detect full-span synteny blocks
    block_span_counter = 1
    block_lines = []
    while line:
        if line.split()[0] == str(block_span_counter):
            block_span_counter += 1
            block_lines.append(line)
        else:
            block_span_counter = 1
            block_lines.clear()
        print(2)
        # Write full-span synteny block
        if block_span_counter == num_of_seqs + 1:
            with open("./synteny_block_alignments/" + str(full_span_synteny_block_counter) + "_block.fna", "w") as g:
                print(3)
                for block_line in block_lines:
                    words = block_line.split()
                    seq_id = words[0]
                    strand = words[1]
                    start = int(words[2])
                    end = int(words[3])
                    accession_code = seq_id_to_accession_code_dict[seq_id]
                    print("About to retrieve sequence from ../../fnas/" + accession_code + ".fna")
                    sequence = SeqIO.read("../../fnas/" + accession_code + ".fna", "fasta")
                    print("Successfully retrieved sequence from ../../fnas/" + accession_code + ".fna")
                    block_sequence = str(sequence.seq)

                    # Invert block_sequence if it is on the opposite strand
                    if strand == "+":
                        block_sequence = block_sequence[start:end]
                    elif strand == "-":
                        block_sequence = block_sequence[end:start]
                        block_sequence = block_sequence[::-1]

                    g.write(">" + accession_code + str(len(block_sequence)) + "\n" +
                            block_sequence + "\n")

            full_span_synteny_block_counter += 1
        line = f.readline()

print("End of align_synteny_blocks.py.")

