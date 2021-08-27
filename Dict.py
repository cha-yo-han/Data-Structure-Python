import sys
import numpy as np


np.random.seed(1)
a = np.random.randn(100)


print(a)

for i in range(100):
    max = a[0]
    if max < a[i]:
        max = a[i]

print(max) 