import sys

# Calculates length of core genome, i.e. the total length of all full-span synteny blocks in blocks_coords.txt
# Takes one argument for min_block_span, the size of the genome sample

# Handle command line arguments
min_block_span = 0
if len(sys.argv) == 1:
    print("Error: No argument given.")
    sys.exit()
else:
    min_block_span = int(sys.argv[1])

# Find synteny blocks in maf2synteny output, blocks_coords.txt
with open("blocks_coords.txt", "r") as f:
    # Check the Seq_id value of the first sequence in the header. If this value is greater than 1, then the initial
    # sequences in the sample, as determined by Seq_id value, will never appear in a synteny block
    line = f.readline()
    line = f.readline()
    block_span_counter_initial_value = int(line.split()[0])

    # Skip past header of blocks_coords.txt
    while line[0] != "-":
        line = f.readline()

    # Start looking for full-span synteny blocks
    full_span_synteny_block_counter = 0
    total_core_genome_length = 0
    block_span_counter = block_span_counter_initial_value
    while line:
        # Check whether the next line encodes the synteny block in the next genome sequence
        if line.split()[0] == str(block_span_counter):
            block_span_counter += 1
        else:
            block_span_counter = block_span_counter_initial_value

        # True when a new block with sufficient span has been detected
        if block_span_counter == min_block_span + 1:
            block_span_counter = block_span_counter_initial_value
            full_span_synteny_block_counter += 1
            total_core_genome_length += int(line.split()[4])

        line = f.readline()

print(str(full_span_synteny_block_counter) + "," + str(total_core_genome_length))

