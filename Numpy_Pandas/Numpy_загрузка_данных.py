import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('https://video.ittensive.com/python-advanced/01.mnist.8.txt',
                  delimiter=',', skiprows=1, max_rows=1)
data = np.reshape(data, (28, 28))
plt.imshow(data, cmap='Greys')
plt.show()
