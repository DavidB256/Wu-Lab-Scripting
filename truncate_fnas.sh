#!/bin/bash

# Removes all sequences after the first one from all FNA files in "dir" directory and writes truncated copies to "output" directory with numbered file names
# Takes flag "-d" for input directory "dir" and flag "-o" for output directory "output"

# Handling flags
while getopts ":d:o:" flag
do
  case "$flag" in
    d) dir="$OPTARG";;
    o) output="$OPTARG";;
    \?) echo "Unrecognized flag."
  esac
done

# Iterating through files in "dir"
for file in ${dir}*.fna
do
  truncate_line_number=`grep -n ">" $file | head -2 | tail -1 | cut -d : -f1`
  ((truncate_line_number--))
  fasta_header_array=($(head -n 1 $file))
  accession_code=${fasta_header_array:1}
  if [ $truncate_line_number -eq 0 ]
  then
    cp $file "${output}${accession_code}.fna"
  else
    ((line--))
    head -n$truncate_line_number $file > "${output}${accession_code}.fna"
  fi
done

