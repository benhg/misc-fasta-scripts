#!/local/cluster/bin/python3                                                                                                 

import re
import sys

if len(sys.argv) != 3:
    print("Usage: python3 convert_fasta_C_motif.py <input_file> <output_file>")
    exit(1)
infile  = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
regex = re.compile(r".*[A-BD-Z]+C[A-BD-Z]+C[A-BD-Z]+CC[A-BD-Z]+C[A-BD-Z]+C[A-BD-Z]+.*")
in_text = infile.readlines()


for i, line in enumerate(in_text):
    if '>' in line:
        if bool(re.match(regex, in_text[i+1])):
            outfile.write(in_text[i])
            outfile.write(in_text[i+1])


