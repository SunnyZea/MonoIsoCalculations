import os
import json


print("Please provide the working directory: ")
working_dir = input()

print("Please enter the file: ")
file = input()

fasta_dict = {}

with open(file, 'r') as fastafile:
    first_line = fastafile.readline()
    key = first_line.split('|')[1]
    #print(key)

    lines = fastafile.readlines()[0:]
    string = ''.join(lines)
    value1 = string.split('\n')
    value = ''.join(value1)
    #print(value)

    fasta_dict[key] = value

#print(fasta_dict)

new_file = input("Please name your new file: ")
f2 = open(os.path.join(working_dir, new_file), "w")

for i in fasta_dict:
    f2.write(str(i) + '\t' + str(fasta_dict[i]))

f2.close()


