import sys

# Counts the numbers of occurrences of different seq_id values in blocks_coords.txt, given the maximum seq_id value

# Handle command line arguments
size = 1
if len(sys.argv) == 1:
    print("Error: No argument given.")
    sys.exit()
else:
    size = int(sys.argv[1])

seq_id_counts = [0 for i in range(size)]

with open("blocks_coords.txt", "r") as f:
    # Skip header
    line = f.readline()
    while line[0] != "-":
        line = f.readline()
    # Read through remainder of file
    while line:
        first_word = line.split()[0]
        if first_word.isnumeric():
            seq_id_counts[int(first_word) - 1] += 1
        line = f.readline()

# Format and print output
output_string = ""
for i in seq_id_counts:
    output_string += str(i)
    output_string += ","
output_string = output_string[:-1]
print(output_string)

