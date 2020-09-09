import os
import math

def logfac(a, b):
    n = 0
    for x in range(a, b, -1):
        n += math.log(x)
    return n

print('Please provide the working directory: ')
working_dir = input()

print('Please enter the file: ')
file = input()

print('Please enter the protein name: ')
name = input()

with open (file, 'r') as f:
    ffile = f.readline()
    lines = ffile.split('\t')[1]
    print('The fasta sequence is: ', lines)

res = {'A': {'C': 3, 'H': 5, 'N': 1, 'O': 1, 'S': 0},
       'R': {'C': 6, 'H': 12, 'N': 4, 'O': 1, 'S': 0},
       'N': {'C': 4, 'H': 6, 'N': 2, 'O': 2, 'S': 0},
       'D': {'C': 4, 'H': 5, 'N': 1, 'O': 3, 'S': 0},
       'C': {'C': 3, 'H': 5, 'N': 1, 'O': 1, 'S': 1},
       'Q': {'C': 5, 'H': 8, 'N': 2, 'O': 2, 'S': 0},
       'E': {'C': 5, 'H': 7, 'N': 1, 'O': 3, 'S': 0},
       'G': {'C': 2, 'H': 3, 'N': 1, 'O': 1, 'S': 0},
       'H': {'C': 6, 'H': 7, 'N': 3, 'O': 1, 'S': 0},
       'I': {'C': 6, 'H': 11, 'N': 1, 'O': 1, 'S': 0},
       'L': {'C': 6, 'H': 11, 'N': 1, 'O': 1, 'S': 0},
       'K': {'C': 6, 'H': 12, 'N': 2, 'O': 1, 'S': 0},
       'M': {'C': 5, 'H': 9, 'N': 1, 'O': 1, 'S': 1},
       'F': {'C': 9, 'H': 9, 'N': 1, 'O': 1, 'S': 0},
       'P': {'C': 5, 'H': 7, 'N': 1, 'O': 1, 'S': 0},
       'S': {'C': 3, 'H': 5, 'N': 1, 'O': 2, 'S': 0},
       'T': {'C': 4, 'H': 7, 'N': 1, 'O': 2, 'S': 0},
       'W': {'C': 11, 'H': 10, 'N': 2, 'O': 1, 'S': 0},
       'Y': {'C': 9, 'H': 9, 'N': 1, 'O': 2, 'S': 0},
       'V': {'C': 5, 'H': 9, 'N': 1, 'O': 1, 'S': 0}}

c_num = 0
h_num = 0
n_num = 0
o_num = 0
s_num = 0
p_num = 0

for i in lines:
    c_num = c_num + res[i]['C']
    h_num = h_num + res[i]['H']
    n_num = n_num + res[i]['N']
    o_num = o_num + res[i]['O']
    s_num = s_num + res[i]['S']

h_num = h_num + 2
o_num = o_num + 1

molecular_formula = 'C' + str(c_num) + 'H' + str(h_num) + 'N' + str(n_num) + 'O' + str(o_num) + 'S' + str(s_num)
print('The molecular formula is: ', molecular_formula)

#user input thingie

print('Please enter the number of Carbon added via protein modification: ')
c_input = int(input())

print('Please enter the number of Hydrogen added via protein modification: ')
h_input = int(input())

print('Please enter the number of Nitrogen added via protein modification: ')
n_input = int(input())

print('Please enter the number of Oxygen added via protein modification: ')
o_input = int(input())

print('Please enter the number of Sulfur added via protein modification: ')
s_input = int(input())

print('Please enter the number of Phosphorus added via protein modification: ')
p_input = int(input())

c_num = c_num + c_input
h_num = h_num + h_input
n_num = n_num + n_input
o_num = o_num + o_input
s_num = s_num + s_input
p_num = p_num + p_input

modified_formula = 'C' + str(c_num) + 'H' + str(h_num) + 'N' + str(n_num) + 'O' + str(o_num) + 'S' + str(s_num) + 'P' + str(p_num)
print('The modified molecular formula is: ', modified_formula)

iso = {'C': {'C12': [12, 0.9893], 'C13': [13.00335483778, 0.0107]},
      'H': {'H1': [1.00782503207, 0.999885], 'H2': [2.01410177785, 0.000115]},
      'N': {'N14': [14.00307400478, 0.99632], 'N15': [15.00010889823, 0.00368]},
      'O': {'O16': [15.99491461956, 0.99757], 'O17': [16.999131703, 0.00038], 'O18': [17.999161001, 0.00205]},
      'S': {'S32': [31.972070999, 0.9493], 'S33': [32.971458759, 0.0076], 'S34': [33.967866902, 0.0429], 'S36': [35.96708076, 0.0002]},
      'P': {'P31': [30.973762, 1.0]}}

avg_c = iso['C']['C12'][0] * iso['C']['C12'][1] + iso['C']['C13'][0] * iso['C']['C13'][1]
avg_h = iso['H']['H1'][0] * iso['H']['H1'][1] + iso['H']['H2'][0] * iso['H']['H2'][1]
avg_n = iso['N']['N14'][0] * iso['N']['N14'][1] + iso['N']['N15'][0] * iso['N']['N15'][1]
avg_o = iso['O']['O16'][0] * iso['O']['O16'][1] + iso['O']['O17'][0] * iso['O']['O17'][1] + iso['O']['O18'][0] * iso['O']['O18'][1]
avg_s = iso['S']['S32'][0] * iso['S']['S32'][1] + iso['S']['S33'][0] * iso['S']['S33'][1] + iso['S']['S34'][0] * iso['S']['S34'][1] + iso['S']['S36'][0] * iso['S']['S36'][1]
avg_p = iso['P']['P31'][0] * iso['P']['P31'][1]

avg_mass = avg_c * c_num + avg_h * h_num + avg_n * n_num + avg_o * o_num + avg_s * s_num + avg_p * p_num

predict = []

print('The average mass is: ', avg_mass)

mono_mass = iso['C']['C12'][0] * c_num + iso['H']['H1'][0] * h_num + iso['N']['N14'][0] * n_num + iso['O']['O16'][0] * o_num + iso['S']['S32'][0] * s_num + iso['P']['P31'][0] * p_num

print('The smallest mass is: ', mono_mass)

bobert = int(avg_mass - mono_mass) * 2 + 10 # welp i guess we're screwed fam

for i in range(c_num + 1):
    if i > bobert:
        break
    c_itr = (c_num - i) * math.log(iso['C']['C12'][1]) + i * math.log(iso['C']['C13'][1]) + logfac(c_num, c_num - i) - logfac(i, 0)
    for j in range(h_num + 1):
        if j > bobert - i:
            break
        h_itr = (h_num - j) * math.log(iso['H']['H1'][1]) + j * math.log(iso['H']['H2'][1]) + logfac(h_num, h_num-j) - logfac(j, 0)
        for k in range(n_num + 1):
            if k > bobert - i - j:
                break
            n_itr = (n_num - k) * math.log(iso['N']['N14'][1]) + k * math.log(iso['N']['N15'][1]) + logfac(n_num, n_num - k) - logfac(k, 0)
            for l in range(o_num + 1):
                if l > bobert - i - j - k:
                    break
                for l1 in range(o_num + 1 - l):
                    if 2 * l1 > bobert - i - j - k - l:
                        break
                    o_itr = ((o_num - l - l1) * math.log(iso['O']['O16'][1]) + l * math.log(iso['O']['O17'][1]) + l1 * math.log(iso['O']['O18'][1]) +
                             logfac(o_num, o_num - l - l1) - logfac(l, 0) - logfac(l1, 0))
                    for m in range(s_num + 1):
                        if m > bobert - i - j - k - l - 2 * l1:
                            break
                        for m1 in range(s_num + 1 - m):
                            if 2 * m1 > bobert - i - j - k - l - 2 * l1 - m:
                                break
                            for m2 in range(s_num + 1 - m - m1):
                                if 4 * m2 > bobert - i - j - k - l - 2 * l1 - m - 2 * m1:
                                    break
                                s_itr = ((s_num - m - m1 - m2) * math.log(iso['S']['S32'][1]) + m * math.log(iso['S']['S33'][1]) + m1 * math.log(iso['S']['S34'][1]) +
                                         m2 * math.log(iso['S']['S36'][1]) + logfac(s_num, s_num - m - m1 - m2) - logfac(m, 0) - logfac(m1, 0) - logfac(m2, 0))

                                iso_mass = ((c_num - i) * iso['C']['C12'][0] + i * iso['C']['C13'][0] + (h_num - j) * iso['H']['H1'][0] + j * iso['H']['H2'][0] +
                                            (n_num - k) * iso['N']['N14'][0] + k * iso['N']['N15'][0] + (o_num - l - l1) * iso['O']['O16'][0] + l * iso['O']['O17'][0] +
                                            l1 * iso['O']['O18'][0] + (s_num - m - m1 - m2) * iso['S']['S32'][0] + m * iso['S']['S33'][0] + m1 * iso['S']['S34'][0] +
                                            m2 * iso['S']['S36'][0] + (p_num) * iso['P']['P31'][0])

                                abundance = math.exp(c_itr + h_itr + n_itr + o_itr + s_itr + p_num * math.log(iso['P']['P31'][1]))
                                mass = round(iso_mass, 1)
                                weight = round(abundance, 6)
                                predict.append([mass, weight])
         
simulation = {}

new_file = input('Please name your new file: ')
f2 = open(os.path.join(working_dir, new_file), 'w')

for i in predict:
        if i[0] not in simulation:
            simulation[i[0]] = i[1]
        else:
            simulation[i[0]] += i[1]

min_amt = min(simulation) - 2
max_amt = max(simulation)

richard = int((max_amt - min_amt) * 10)

for i in range(0, richard):
    if min_amt + i * 0.1 not in simulation:
        simulation[min_amt + i * 0.1] = 0.0
        
               
for i in sorted(simulation):
    #print(str(i) + '\t' + str(simulation[i]))
    f2.write(str(i) + '\t' + str(simulation[i]) + '\n')

f2.close()

####
print('\t The graph will now be generated.')

print("Please enter the name of your graph: ")
graph = input()

graph_name = graph + '.png'

import matplotlib.pyplot as plt
import numpy as np

d = {}
with open (new_file, 'r') as f:
    for line in f:
        (key, val) = line.split()
        d[float(key)] = float(val)

fig1 = plt.gcf()
plt.plot(list(d.keys()), list(d.values()))

plt.xticks(np.arange(min(list(d.keys())), max(list(d.keys())) + 1, 5.0))

Henry = 'Monoisotopic Peaks of ' + name
plt.title(Henry)

plt.ylabel('Abundance')
plt.xlabel('Weight')

plt.show()
plt.draw()

fig1.savefig(graph_name)




