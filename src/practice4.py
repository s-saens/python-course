import random
import numpy as np;

l = list(map(int, input().split()))

l.sort();

print(l)
 


size = 5
numpyArr = np.random.randint(1, 30, (size, size))

print(numpyArr)

numpyArr = numpyArr * random.randint(1, 10)

print(numpyArr)