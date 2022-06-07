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
    # Skip past header of blocks_coords.txt
    line = f.readline()
    while line[0] != "-":
        line = f.readline()

    # Start looking for full-span synteny blocks
    synteny_block_counter = 0
    core_genome_length = 0
    block_span_counter = 0
    seq_ids_in_block = []
    while line:
        # Check whether the next line encodes a synteny block from a unique genome
        seq_id = line.split()[0]
        if seq_id.isnumeric():
            if seq_id not in seq_ids_in_block:
                block_span_counter += 1
                seq_ids_in_block.append(seq_id)
        else:
            # Reset
            block_span_counter = 0
            seq_ids_in_block.clear()

        # True when a new block with sufficient span has been detected
        if block_span_counter == min_block_span:
            # Reset
            block_span_counter = 0
            seq_ids_in_block.clear()
            synteny_block_counter += 1
            core_genome_length += int(line.split()[4])

            # Skip ahead to next block
            while line[0] != "-":
                line = f.readline()

        line = f.readline()

print(str(synteny_block_counter) + "," + str(core_genome_length))
