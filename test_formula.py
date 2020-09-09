import os
import math

print("please provide the working directory:")
working_dir = input()

print("""please provide the file name you want to use to calculate mass distribution.
The program only recognize one-letter residue codes such as in a FASTA file. File name: """)

file = input()

f1 = open(os.path.join(working_dir, file))
seq = f1.read().splitlines()

if seq[0][0] == ">":
    seq = "".join(seq[1:])
else:
    seq ="".join(seq)

f1.close()

res = {"A": {"C": 3, "H": 5, "N": 1, "O": 1, "S": 0},
       "R": {"C": 6, "H": 12, "N": 4, "O": 1, "S": 0},
       "N": {"C": 4, "H": 6, "N": 2, "O": 2, "S": 0},
       "D": {"C": 4, "H": 5, "N": 1, "O": 3, "S": 0},
       "C": {"C": 3, "H": 5, "N": 1, "O": 1, "S": 1},
       "Q": {"C": 5, "H": 8, "N": 2, "O": 2, "S": 0},
       "E": {"C": 5, "H": 7, "N": 1, "O": 3, "S": 0},
       "G": {"C": 2, "H": 3, "N": 1, "O": 1, "S": 0},
       "H": {"C": 6, "H": 7, "N": 3, "O": 1, "S": 0},
       "I": {"C": 6, "H": 11, "N": 1, "O": 1, "S": 0},
       "L": {"C": 6, "H": 11, "N": 1, "O": 1, "S": 0},
       "K": {"C": 6, "H": 12, "N": 2, "O": 1, "S": 0},
       "M": {"C": 5, "H": 9, "N": 1, "O": 1, "S": 1},
       "F": {"C": 9, "H": 9, "N": 1, "O": 1, "S": 0},
       "P": {"C": 5, "H": 7, "N": 1, "O": 1, "S": 0},
       "S": {"C": 3, "H": 5, "N": 1, "O": 2, "S": 0},
       "T": {"C": 4, "H": 7, "N": 1, "O": 2, "S": 0},
       "W": {"C": 11, "H": 10, "N": 2, "O": 1, "S": 0},
       "Y": {"C": 9, "H": 9, "N": 1, "O": 2, "S": 0},
       "V": {"C": 5, "H": 9, "N": 1, "O": 1, "S": 0}}

c_no = 0
h_no = 0
n_no = 0
o_no = 0
s_no = 0

res_no = 0
for i in seq:
    c_no += res[i]["C"]
    h_no += res[i]["H"]
    n_no += res[i]["N"]
    o_no += res[i]["O"]
    s_no += res[i]["S"]
    res_no += 1

if res_no > 500:
    raise NameError("The protein has more than 500 residues. If considering to continue, please edit the program to remove this raised error and also find a fast computer to run the program.")

ct_amide = input("Does the protein have a C-terminal amide (Y or N): ")
if ct_amide == "Y" or ct_amide == "y":
    h_no += 3
    n_no += 1
else:
    h_no += 2
    o_no += 1

modification = input("Does the protein has posttranslational modifications (Y or N): ")
if modification == "Y" or modification =="y":
    c_mod = input("Please the additional carbon element no. due to modifications: ")
    h_mod = input("Please the additional hydrogen element no. due to modifications. A modification also require to strip off a hydrogen from a protein: ")
    n_mod = input("Please the additional nitrogen element no. due to modifications: ")
    o_mod = input("Please the additional oxygen element no. due to modifications: ")
    s_mod = input("Please the additional sulfur element no. due to modifications: ")
    c_no += int(c_mod)
    h_no += int(h_mod)
    n_no += int(n_mod)
    o_no += int(o_mod)
    s_no += int(s_mod)

formular ="C" + str(c_no) + "H" + str(h_no) + "N" + str(n_no) + "O" + str(o_no) + "S" + str(s_no)

print("the formular of the protein is", formular)
