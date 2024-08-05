import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [10,20,30,40,50]

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# plt.plot(x,y)
# plt.show()

# plot graph without line 
# plt.plot(x,y,"o")
# plt.show()

