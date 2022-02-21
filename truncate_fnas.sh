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

counter=0

# Iterating through files in "dir"
for file in ${dir}*.fna
do
  line=`grep -n ">" $file | head -2 | tail -1 | cut -d : -f1`
  if [ $line -eq 1 ]
  then
    cp $file "${output}${counter}.fna"
  else
    ((line--))
    head -n$line $file > "${output}${counter}.fna"
  fi
  ((counter++))
done
