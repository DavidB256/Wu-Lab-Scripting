import sys

# Counts the number of non-repetitive synteny blocks with span greater than or equal to a given threshold
# in SibeliaZ output file blocks_coords.gff
# Calculates the total length of counted synteny blocks

# Object instantiated for each synteny block
class Block:
    def __init__(self, lines):
        self.lines = lines
        self.nonunique_span = len(lines)
        self.is_nonrepetitive = self.determine_is_nonrepetitive()
        self.initial_length = int(lines[0].split()[4]) - int(lines[0].split()[3])

    # Returns "True" iff there are no repeated accession codes in "self.lines"
    def determine_is_nonrepetitive(self):
        accession_codes = []
        for line in self.lines:
            accession_code = line.split()[0]
            if accession_code in accession_codes:
                return False
            accession_codes.append(accession_code)
        return True


# Handle command line arguments
if len(sys.argv) < 2:
    print("Error: At least one command line argument is required.")
    sys.exit()
if not sys.argv[1].isnumeric():
    print("Error: Integer argument not provided.")
    sys.exit()
threshold = int(sys.argv[1])

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
            blocks.append(Block(block_lines))
            block_lines.clear()
            break
        if line.split()[8] != seq_id:
            seq_id = line.split()[8]
            blocks.append(Block(block_lines))
            block_lines.clear()

# Iterate through list of Blocks objects, blocks
block_counter = 0
total_initial_length = 0
for block in blocks:
    if block.is_nonrepetitive and block.nonunique_span >= threshold:
        block_counter += 1
        total_initial_length += block.initial_length

print(block_counter, total_initial_length, sep=",")
