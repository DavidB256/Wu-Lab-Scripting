#!/bin/bash

dirs="out_a4352_m25 out_a4352_m50 out_a4352_m100 out_a4352_m200 out_a4352_m500"
op="/scratch/djb3ve/sibeliaz/truncated2176/largest_synteny_block_spans.csv"

# Cleaning up
if [ -f $op ]; then
        rm $op
fi
if [ -f nohup.out ]; then
        rm nohup.out
fi

# Write header of output CSV file
echo "m,span_with_repeats,span" >> $op

for dir in $dirs; do
	cd $dir

	# Print to console
	echo -n $dir
	echo -n -e "\t"
	echo `date`

	# Print to output CSV file
	m=`echo $dir | grep -Eo '[0-9]+$'`
	echo -n $m >> $op
	echo -n "," >> $op
	echo -n `cat blocks_coords.gff | awk '$9=="id=1"' | wc -l` >> $op
	echo -n "," >> $op
	echo `cat blocks_coords.gff | awk '$9=="id=1"' | awk '{print $1}' | sort | uniq | wc -l` >> $op
	
	cd ..
done