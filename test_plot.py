print('\t The graph will now be generated.')

import matplotlib.pyplot as plt

print('Please provide the working directory: ')
working_dir = input()

print('Please enter the file: ')
file = input()

d = {}
with open (file, 'r') as f:
    for line in f:
        (key, val) = line.split()
        d[float(key)] = float(val)
        #print(d)

fig1 = plt.gcf()
plt.scatter(list(d.keys()), list(d.values()))
plt.plot(list(d.keys()), list(d.values()))
plt.show()
plt.draw()

fig1.savefig('fasta.png')
