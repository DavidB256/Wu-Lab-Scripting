#!/bin/bash

# Iterates through maf2synteny output directories and runs count_synteny_blocks on each blocks_coords.txt file
# in oder to count the number of synteny blocks span at least the given number of genomes, min

# Handling flags
while getopts ":m:" flag; do
	case $flag in
		m) min=$OPTARG;;
		\?) echo "Unrecognized flag."
	esac
done

# Setup
py="/home/davidb/Desktop/scripts/count_synteny_blocks.py"
output="synteny_block_counts.csv"

# Purge preexisting output file
if [ -f $output ]; then
	rm $output
fi

# Iterate through directories in working directory
for file in *; do
	if [ -d $file ]; then
		cd $file
		echo `pwd`
		echo -n "${file}," >> "../${output}"
		python $py $min >> "../${output}"
		cd ../
	fi
done
