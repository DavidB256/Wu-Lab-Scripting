#!/bin/bash

ts="200 250"
as="500"
ms="25 50 100 200 500"
op="`pwd`/nonrepetitive_block_counts.csv"
py="/scratch/djb3ve/sibeliaz/scripts/count_nonrepetitive_blocks.py"

if [ -f $op ]; then
        rm $op
fi

echo "threshold,a,m,count" >> $op

for t in $ts; do
	for a in $as; do
		for m in $ms; do
			cd "out_a${a}_m${m}"
		
				echo -n "${t},${a},${m}," >> $op
				python $py $t >> $op
			
			cd ..
		done
	done
done
