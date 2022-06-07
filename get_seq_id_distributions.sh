#!/bin/bash

# Setup
op="/home/davidb/Desktop/working_sibeliaz/truncated_all/seq_id_distributions.csv"
py="/home/davidb/Desktop/scripts/get_seq_id_distribution.py"
prefix="sibeliaz_out_"
size=2179

# Remove output file from previous run
if [ -f $op ]; then
	rm $op
fi

# Write CSV header
echo -n "m,b," >> $op
for i in $(seq 1 $size); do
	echo -n "${i}" >> $op
	if [ $i -lt $size ]; then
		echo -n "," >> $op
	fi
done
echo >> $op

for mdir in ${prefix}*; do
	cd $mdir
	echo ${mdir//[!0-9]/}
	
	for bdir in *; do
		if [ -d $bdir ]; then
			cd $bdir
			echo "     $bdir"
			echo -n "${mdir//[!0-9]/},${bdir}," >> $op
			
			python $py $size >> $op
			
			cd ../
		fi
	done
	
	cd ../
done