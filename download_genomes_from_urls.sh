#!/bin/bash

# Uses "wget" to download the first "count" many URLs from "file" into "output" directory
# Requires flags "-f" for input file, "-c" for number of files to be downloaded, and "-o" for output directory
# Created for use with FNA GZ files from "assembly_summary_refseq.txt"

while getopts ":f:c:o:" flag
do
  case "$flag" in
    f) file="$OPTARG";;
    c) count=$OPTARG;;
    o) output="$OPTARG";;
    \?) echo "Unrecognized flag."
  esac
done

# Download the first "count" many URLs from "file" into "output"
head -$count $file |
while read line
do
  wget -qP $output $line
done

# This line is supposed to unzip all downloaded .gz files, but it does not work
#gzip -d "${output}*"
