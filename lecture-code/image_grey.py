import matplotlib.pyplot as plt
import numpy as np

m = np.zeros([10, 10])
m[4:6, :] = 1       # set columns 4:6
m[:, 4:6] = 1       # set columns 4:6

# show the image in a figure
plt.imshow(m, cmap='Greys')
plt.xticks([])
plt.yticks([])

# save the figure
plt.savefig('image_grey.png')

plt.show()