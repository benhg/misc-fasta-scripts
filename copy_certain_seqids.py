#!/local/cluster/bin/python3

import re
import sys

if len(sys.argv) != 3:
    print("Usage: python3 {} <input_file> <output_file>".format(__file__))
    exit(1)
infile  = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
in_text = infile.readlines()


for i, line in enumerate(in_text):
    if 'seqID' in line or line.startswith('>'):
        if line in  in_text[i]:
            outfile.write(in_text[i])
            j = i+1
            while not (line[j].startswith('>')):
                outfile.write(line[j])
            i = j
