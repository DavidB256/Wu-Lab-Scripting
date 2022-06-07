#!/bin/bash

# Iterates through SibeliaZ output files in directories named "out_a${a}_m${m}"

as="500"
ms="25 50 100 200 500"
op="`pwd`/synteny_blocks_with_unique_span_above_threshold_count.csv"
threshold=$1

if [ -f $op ]; then
        rm $op
fi

echo "a,m,count" >> $op

for a in $as; do
	for m in $ms; do
		cd "out_a${a}_m${m}"
	
		count=0
		i=1
		while true; do
			unique_span=`cat blocks_coords.gff | awk -v i=$i '$9=="id="i' | awk '{print $1}' | sort | uniq | wc -l`
			
			if [ $unique_span -ge $threshold ]; then
				let count++
			fi
			if [ $unique_span -eq 0 ]; then
				break
			fi
			
			let i++
		done
		
		echo "${a},${m},${count}"
		echo "${a},${m},${count}" >> $op
		
		cd ..
	done
done

