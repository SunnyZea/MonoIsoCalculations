import os
import json

fasta_dict = {}

with open('P63165.txt', 'r') as fastafile:
    first_line = fastafile.readline()
    key = first_line.split('|')[1]
    #print(key)

    lines = fastafile.readlines()[0:]
    string = ''.join(lines)
    value1 = string.split('\n')
    value = ''.join(value1)
    #print(value)

    fasta_dict[key] = value

for i in fasta_dict:
    print(i, fasta_dict[i])
