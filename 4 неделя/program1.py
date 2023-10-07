import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [225, 211, 199, 183, 169, 155, 143, 115, 96, 87]
y1 = [1200, 1100, 1050, 950, 900, 800, 750, 600, 500, 450]
divx = 1
divy = 25

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

x = [0, 250]

z = np.polyfit(x1,y1, 1)
p = np.poly1d(z)
b1 = p(x)
ax1.plot(x, b1, 'r')

ax1.set_xlim([0,250])
ax1.set_ylim([0,1300])

ax1.scatter(x1, y1, marker = '.')

ax1.errorbar(x1, y1, yerr=divy, xerr = divx, color = 'k', linestyle = 'None')

plt.title('График зависимости напряжения от силы тока', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('I, mA')
plt.ylabel('U, mB')

ax1.grid()

plt.show()