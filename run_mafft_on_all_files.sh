#!/bin/bash

# Runs MAFFT with default settings on every FNA file in working directory and outputs 
# into mafft_aligned_synteny_blocks subdirectory.

# Create mafft_aligned_synteny_blocks subdirectory if it does not already exist
if [ -d "mafft_aligned_synteny_blocks" ]; then
	echo "Directory mafft_aligned_synteny_blocks already exists."
else
	echo "Creating directory mafft_aligned_synteny_blocks/"
	mkdir mafft_aligned_synteny_blocks
fi

# Iterate through all FNA files in working directory
for file in *.fna; do
	mafft --thread -1 $file > "mafft_aligned_synteny_blocks/mafft_${file}"
done
