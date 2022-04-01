import sys

# Counts the numbers of occurrences of a given seq_id value in blocks_coords.txt

# Handle command line arguments
if len(sys.argv) == 1:
    print("Error: No argument given.")
    sys.exit()
else:
    seq_id = sys.argv[1]

total = 0
with open("blocks_coords.txt", "r") as f:
    # Skip header
    line = f.readline()
    while line[0] != "-":
        line = f.readline()
    # Read through remainder of file
    while line:
        if line.split()[0] == seq_id:
            total += 1
        line = f.readline()

print(total)

