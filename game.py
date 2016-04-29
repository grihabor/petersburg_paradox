import numpy as np
import matplotlib.pyplot as plt
from random import *

n = 100000
powers = []
means = [0]

for i in range(n):
    j = 1
    while randint(0, 1) == 0:
        j += 1
    powers.append(j)
    t = means[-1] + 2 ** j
    means.append(t)
    
for i in range(1, n+1):
    means[i] /= i

m = np.max(powers)
print('max: ', m)
print('max prize: ', 2 ** m)
print('last mean: ', means[-1])
fs = 24

plt.subplot(121)  
hist,b = np.histogram(powers, bins=m) 
print(len(hist))
plt.bar(np.arange(1, m+1), hist)
plt.ylabel('Number of games', fontsize=fs)
plt.xlabel('Power of 2', fontsize=fs)

plt.subplot(122)
plt.plot(means)
plt.xlabel('Number of games', fontsize=fs)
plt.ylabel('Mean prize', fontsize=fs)

plt.show()
