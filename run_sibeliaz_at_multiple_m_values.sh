#!/bin/bash

op="wrapper_sibeliaz_output.txt"
ip="fnas/*.fna"
ms=(25 50 100 200 500 1000)
as=(150 500 1000)

if [ -f $op ]; then
	rm $op
fi

echo "Starting at `date`." >> $op
for m in ${ms[@]}; do
	for a in ${as[@]}; do
		sibeliaz -n -k 15 -m $m -a $a -o "sibeliaz_out_m${m}_a${a}" $ip
		echo "m=${m}, a=${a} job complete at `date`." >> $op	
	done
done
echo "Ending at `date`." >> $op
