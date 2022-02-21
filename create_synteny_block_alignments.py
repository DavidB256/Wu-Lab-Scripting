
import sys
import os

# Check that the script is being run from a directory that contains "blocks_coords.gff"
if not os.path.exists("blocks_coords.gff"):
    print("Error: \"blocks_coords.gff\" not present.")
    sys.exit()

# Check that an argument is given for the maf2synteny output directory name
if len(sys.argv) >= 2:
    dir = sys.argv[1]
else:
    print("Error: No maf2synteny output directory given.")
    sys.exit()

seq_codes = {}

with open("blocks_coords.gff", "r") as bcg:
    line = bcg.readline()
    while True:
        line = bcg.readline()
        if line[0] != "#":
            break

        seq_codes[line.split()[1]] = len(seq_codes)

    bcg.close()

seq_ids = ["" for i in range(len(seq_codes))]

with open(dir + "blocks_coords.txt") as bct:
    line = bct.readline()

    for i in range(len(seq_codes)):
        line = bct.readline()
        seq_ids[int(line.split()[0])-1] = seq_codes[line.split()[2]]

    counter = 0
    total = 0
    while True:
        line = bct.readline()

        if not line:
            break

        if line.split()[0] == "1":
            counter = 1
            while line.split()[0] == str(counter):
                line = bct.readline()
                counter += 1
                
                if counter == 100:
                    total += 1
                    print(total)

    bct.close()


