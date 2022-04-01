#!/bin/bash

if [ -f "blocks_coords.txt" ]; then
	echo "blocks_coords.txt found."
else
	echo "Error: blocks_coords.txt not found."
	exit 1
fi

if [ -d "synteny_block_alignments" ]; then
	echo "Directory synteny_block_alignments already exists."
else
	echo "Creating directory synteny_block_alignments."
	mkdir synteny_block_alignments
fi

grep ">" ../../fnas/*.fna > grep_output.txt

python ~/Desktop/scripts/align_synteny_blocks.py

echo "End of align_synteny_blocks.sh."

