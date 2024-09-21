import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

values1 = np.random.normal(0, 10, 1000000)
values2 = np.random.normal(0, 10, 100000)
values3 = np.random.normal(0, 10, 10000)
values4 = np.random.normal(0, 10,1000)

ax1.hist(values1, 500)
ax1.grid()
ax2.hist(values2, 250)
ax2.grid()
ax3.hist(values3, 100)
ax3.grid()
ax4.hist(values4, 50)
ax4.grid()

plt.show()