import numpy as np

'''
x = blah, we want another one but not the same one with a different name.

'''

x = np.linspace(10, 12, num=3)
y = np.copy(x)

y[0] = 0.0

print(x)
print(y)