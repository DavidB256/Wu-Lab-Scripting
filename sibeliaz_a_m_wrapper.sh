#!/bin/bash
#SBATCH --mem=100G
#SBATCH --time=24:00:00
#SBATCH --partition standard
#SBATCH --account=igemkoz
#SBATCH -c 16

# Handling flags
while getopts ":a:m:" flag; do
	case $flag in
		a) a=$OPTARG;;
		m) m=$OPTARG;;
		\?) echo "Unrecognized flag."
	esac
done

ip="/scratch/djb3ve/sibeliaz/truncated10/fnas/*.fna"
source activate myenv

echo "Starting at `date`."

sibeliaz -n -k -a $a -m $m -o "out_a${a}_m${m}" $ip

echo "Completed at `date`."