import sys

# Counts number of synteny blocks in a given blocks_t
# Takes one argument for min_block_span, the minimum

# Handle command line arguments
min_block_span = 0
if len(sys.argv) == 1:
    print("Error: No argument given.")
else:
    min_block_span = int(sys.argv[1])

# Detect synteny blocks in maf2synteny output, blocks_coords.txt
with open("blocks_coords.txt", "r") as f:
    # Skip past header of blocks_coords.txt
    line = f.readline()
    while line[0] != "-":
        line = f.readline()

    total = 0
    block_span_counter = 0
    seq_ids_in_block = []
    while line:
        seq_id = line.split()[0]
        if seq_id.isnumeric() and seq_id not in seq_ids_in_block:
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
            # Increment total counter
            total += 1

        line = f.readline()

print(total)
