import os

print("Please provide the working directory: ")
working_dir = input()

print("Please enter the file: ")
file = input()

with open (file, 'r') as f:
    ffile = f.readline()
    lines = ffile.split('\t')[1]
    print(lines)

residue = {"A": {"C": 3, "H": 5, "N": 1, "O": 1, "S": 0},
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

carbon = 0
hydrogen = 0
nitrogen = 0
oxygen = 0
sulfur = 0

for i in lines:
    carbon = carbon + residue[i]['C']
    hydrogen = hydrogen + residue[i]['H']
    nitrogen = nitrogen + residue[i]['N']
    oxygen = oxygen + residue[i]['O']
    sulfur = sulfur + residue[i]['S']

hydrogen = hydrogen + 2
oxygen = oxygen + 1

molecular_formula = 'C' + str(carbon) + 'H' + str(hydrogen) + 'N' + str(nitrogen) + 'O' + str(oxygen) + 'S' + str(sulfur)
print(molecular_formula)
