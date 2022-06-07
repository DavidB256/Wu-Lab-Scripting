#!/bin/bash

dirs="sibeliaz_out_100 sibeliaz_out_200 sibeliaz_out_50 sibeliaz_out_1000 sibeliaz_out_25 sibeliaz_out_500"
spans="100 500 1000 2000"
op="/home/davidb/Desktop/working_sibeliaz/truncated_all/core_genome_lengths_vs_m_and_span.csv"
py="/home/davidb/Desktop/scripts/get_core_genome_length.py"

if [ -f $op ]; then
	rm $op
fi

echo "m,span,num_of_blocks,core_genome_length" >> $op

for dir in $dirs; do
	echo $dir
	cd "${dir}/1"
	
	for span in $spans; do
		echo "     $span"
		echo -n "${dir//[!0-9]/},$span," >> $op
		python $py $span >> $op
	done
	
	cd ../../
done