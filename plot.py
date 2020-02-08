import matplotlib.pyplot as plt
import numpy as np

# data from https://catalog.data.gov/dataset/u-s-daily-climate-normals-1981-2010

x = np.arange(0, 20, .5)
y = x**2

plt.plot(x, y, 'r-')
plt.title('y=x^2')
plt.show()