#!/bin/bash

# Iterates through maf2synteny output directories and runs count_synteny_blocks on each blocks_coords.txt file
# in order to count the number of full synteny blocks, i.e. synteny blocks that contain each of the first "m" genomes
# exactly once
# Practically, "m" should be set equal to the number of genomes in the sample

# Handling flags
while getopts ":m:" flag; do
	case $flag in
		m) min=$OPTARG;;
		\?) echo "Unrecognized flag."
	esac
done

# Setup
py="/home/davidb/Desktop/scripts/count_full_synteny_blocks.py"
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
