#!/bin/bash

# Run from directory containing SibeliaZ output directories
# Creates CSV, with one line per maf2synteny "b" value per SibeliaZ "m" value, containing block length and total
# Requires 2 flags: "s" should be set to the number of genomes in the sample, "p" should be set to the prefix of SibeliaZ 
# output directory names in order to differentiate them from other present directories

echo "Starting."

# Handling flags
while getopts ":s:p:" flag
do
  case "$flag" in
    s) span=$OPTARG;;
    p) prefix="$OPTARG";;
    \?) echo "Unrecognized flag."
  esac
done

# Setup
py="/home/davidb/Desktop/scripts/get_core_genome_length.py"
op="`pwd`/core_genome_lengths.csv"
span=10

# Clear pre-existing output file
if [ -f $op ]; then
	rm $op
fi

# Create header
echo "m,b,count,length" >> $op

# Iterate through SibeliaZ outputs
for mdir in ${prefix}*; do
	echo $mdir
	cd $mdir
	#Iterate through maf2synteny outputs
	for bdir in *; do
		if [ -d $bdir ]; then
			cd $bdir
			echo -n "${mdir//[!0-9]/},${bdir}," >> $op
			
			# Run Python script to count number of full-span synteny blocks and core genome length
			python $py $span >> $op
			echo $bdir
			cd ../
		fi
	done
	cd ../
done

echo "Done."

