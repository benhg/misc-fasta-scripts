#!/local/cluster/bin/python3                                                                                                 

import re
import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python3 {} <input_file> <output_file>".format(__file__))
    exit(1)
infile  = open(sys.argv[1], 'r')
output_file = sys.argv[2]
motif_list = [
              {"name":"Araneae",
               "regex": r".*[A-BD-Z]{1}C[A-BD-Z]{6}C[A-BD-Z]{6}CC[A-BD-Z]{19}C[A-BD-Z]{2}C[A-BD-Z]{1}.*"},
               {"name":"Conus",
                "regex": r".*[A-BD-Z]{3}C[A-BD-Z]{6}C[A-BD-Z]{6}CC[A-BD-Z]{4}C[A-BD-Z]{3}C[A-BD-Z]{1}.*"},
               {"name":"Dytrisia",
                "regex": r".*[A-BD-Z]{5,9}C[A-BD-Z]{3}C[A-BD-Z]{9}CC[A-BD-Z]{10}C[A-BD-Z]{5,6}C[A-BD-Z]{1,3}.*"},
               {"name":"Araneaetwo",
                "regex": r".*[A-BD-Z]{0,6}C[A-BD-Z]{4,6}C[A-BD-Z]{4,9}CC[A-BD-Z]{2,10}C[A-BD-Z]{3,14}C[A-BD-Z]{1,16}.*"},
               {"name":"Brachycera",
                "regex": r".*[A-BD-Z]{10}C[A-BD-Z]{6}C[A-BD-Z]{5}CC[A-BD-Z]{3}C[A-BD-Z]{6}C[A-BD-Z]{2}.*"},
               {"name":"Conustwo",
                "regex": r".*[A-BD-Z]{0,6}C[A-BD-Z]{2,7}C[A-BD-Z]{2,9}CC[A-BD-Z]{2,9}C[A-BD-Z]{3,10}C[A-BD-Z]{0,7}.*"},
               {"name":"Hemiptera",
                "regex": r".*[A-BD-Z]{4,5}C[A-BD-Z]{6}C[A-BD-Z]{6}CC[A-BD-Z]{4,5}C[A-BD-Z]{6}C[A-BD-Z]{1,3}.*"},
               {"name":"Scorpiones",
                "regex": r".*[A-BD-Z]{1,4}C[A-BD-Z]{6}C[A-BD-Z]{5}CC[A-BD-Z]{3,5}C[A-BD-Z]{8,10}C[A-BD-Z]{1,6}.*"},
               {"name":"Terebridae",
                "regex": r".*[A-BD-Z]{2,10}C[A-BD-Z]{2,5}C[A-BD-Z]{3,5}CC[A-BD-Z]{4,16}C[A-BD-Z]{2,10}C[A-BD-Z]{1,3}.*"},
             ]


# Araneae (1)C(6)C(6)CC(19)C(2)C(1)
# Conus (3)C(6)C(6)CC(4)C(3)C(1)
# Dytrisia (5-9)C(3)C(9)CC(10)C(5-6)C(1-3)
# Araneaetwo (0-6)C(4-6)C(4-9)CC(2-10)C(3-14)C(1-16)
# Brachycera (10)C(6)C(5)CC(3)C(6)C(2)
# Conustwo (0-6)C(2-7)C(2-9)CC(2-9)C(3-10)C(0-7)
# Hemiptera (4-5)C(6)C(6)CC(4-5)C(6)C(1-3)
# Scorpiones (1-4)C(6)C(5)CC(3-5)C(8-10)C(1-6)
# Terebridae (2-10)C(2-5)C(3-5)CC(4-16)C(2-10)C(1-3)


in_text = infile.readlines()

file = open(output_file, 'w')
writer = csv.writer(file)
writer.writerow(["motif_name","sequence_id", "sequence_contents"])

for motif in motif_list:
    regex = motif['regex']
    print(regex)
    for i, line in enumerate(in_text):
        if '>' in line:
            if bool(re.match(regex, in_text[i+1])):
                print("match")
                seq_id = in_text[i].split(">")[1]
                seq_contents = in_text[i+1]
                print(seq_id, seq_contents)
                writer.writerow([motif['name'], seq_id, seq_contents])
file.close()
