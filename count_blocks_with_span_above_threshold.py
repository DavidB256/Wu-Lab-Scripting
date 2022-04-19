import sys

# Counts number of synteny blocks in blocks_coords.gff with unique span above the threshold given by a command line
# argument
# This is much faster than previous attempts with Bash and on maf2synteny output because it directly reads SibeliaZ
# output

# Handle command line arguments
if len(sys.argv) < 2:
    print("Error: At least one command line argument is required.")
    sys.exit()
if not sys.argv[1].isnumeric():
    print("Error: Integer argument not provided.")
    sys.exit()
threshold = int(sys.argv[1])
if sys.argv[2] == "n":
    mode = 1
else:
    mode = 0

with open("blocks_coords.gff", "r") as f:
    # Setup
    line = f.readline()
    seq_id = line.split()[-1]
    unique_accession_codes = []
    unique_span = 0
    non_unique_span = 0
    block_counter = 0
    total_non_unique_span_of_full_span_blocks = 0
    block_counter_incremented = False
    # Iterate through blocks_coords.gff
    while line:
        non_unique_span += 1
        # If a block with unique span greater than the threshold has been detected, increment block_counter and
        # read ahead to the next block
        if unique_span >= threshold and not block_counter_incremented:
            block_counter += 1
            block_counter_incremented = True
            # Skip ahead to next block if mode==0
            if mode == 0:
                while line.split()[-1] == seq_id:
                    line = f.readline()

        # Upon reaching a new block, reset relevant variables
        if line.split()[-1] != seq_id:
            if unique_span >= threshold:
                total_non_unique_span_of_full_span_blocks += non_unique_span - 1
            block_counter_incremented = False
            non_unique_span = 1
            seq_id = line.split()[-1]
            unique_accession_codes.clear()
            unique_span = 0

        # Increment unique_span if a unique genome in the current block is attested
        if line.split()[0] not in unique_accession_codes:
            unique_accession_codes.append(line.split()[0])
            unique_span += 1

        # Read next line of blocks_coords.gff
        line = f.readline()

# Output
if mode == 0:
    print(block_counter)
elif mode == 1:
    average_non_unique_span_of_full_span_blocks = total_non_unique_span_of_full_span_blocks / block_counter
    print(str(block_counter) + "," + str(average_non_unique_span_of_full_span_blocks))