import math

def logfac(a, b):
    n = 0
    for x in range(a, b, -1):
        n += math.log(x)
    return n

prob = math.exp(990*math.log(0.9803) + 10*math.log(0.0107) + logfac(1000, 990) - math.log(math.factorial(10)))
print(prob)

