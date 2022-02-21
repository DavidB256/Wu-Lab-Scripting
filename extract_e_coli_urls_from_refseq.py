
import sys

# Writes FNA GZ URLs for E. coli from "assembly_summary_refseq.txt" into output file
# First argument is name of input file
# Second (optional) argument is name of output file. Defaults to "e_coli_fna_gz_urls.txt"


if len(sys.argv) >= 2:
    input_file = sys.argv[1]
else:
    print("Error: No input file name given.")
    sys.exit()

if len(sys.argv) >= 3:
    output_file = sys.argv[2]
else:
    print("No output file name given. Defaulting to \"e_coli_fna_gz_urls.txt\"")
    output_file = "e_coli_fna_gz_urls.txt"

with open(output_file, "w") as o:
    with open(input_file, "r") as i:
        while True:
            line = i.readline()
            if ("Escherichia coli" in line) and ("Scaffold" not in line) and ("Contig" not in line):
                words = line.split('\t')
                for word in words:
                    if word[:5] == "https":
                        url1 = word[57:]
                        url2 = "genomic.fna.gz"
                        o.write(word + r"/" + url1 + r"_" + url2 + "\n")
                        break

            if not line:
                break

print("Terminated without error.")
