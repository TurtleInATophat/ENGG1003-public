import numpy as np

"""
At the memory location of x, point y to the same spot.
Nikki = Nikki-kara
"""


x = np.linspace(10, 12, num=3)
y = x       # DON'T do this to copy an array

print(y)
y[0] = 0.0

print(y)    # ... as expected
print(x)    # ... x has changed too!