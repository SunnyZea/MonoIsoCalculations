import math

def logfac(a, b):
    n = 0
    for x in range(a, b, -1):
        n += math.log(x)
    return n

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    for n in range(5-m):
                        abundance = math.exp(logfac(5, i) - math.log(math.factorial(i)) +
                                             logfac(5, j) - math.log(math.factorial(j)) +
                                             logfac(5, k) - math.log(math.factorial(k)) +
                                             logfac(5, l) - math.log(math.factorial(l)) +
                                             math.log(math.factorial(5)) - math.log(math.factorial(m)) - math.log(math.factorial(5-m-n)) - math.log(math.factorial(n)))
                        print(abundance)
 
