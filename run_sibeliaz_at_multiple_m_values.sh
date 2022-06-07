#!/bin/bash

op="output.txt"
ip="fnas/*.fna"
ms=(50 100 200 500 1000 25)

if [ -f $op ]; then
	rm $op
fi

echo "Starting at `date`." >> $op
for i in ${ms[@]}; do
	sibeliaz -n -k 15 -m $i -o "sibeliaz_out_$i" $ip
	echo "m=${i} job complete at `date`." >> $op	
done
echo "Ending at `data`." >> $op
