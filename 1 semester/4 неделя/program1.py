import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [99.7, 200, 308, 411, 521, 615, 727, 820]
y2 = [133.4, 269.1, 404.8, 540.5, 670.2, 809.9, 947.8, 1082.3]
y3 = [160.5, 321.5, 485.1, 644, 805.2, 969, 1132, 1296]
y4 = [155, 312, 469, 625, 783, 942, 1101, 1258]

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

x = [0, 8]

z1 = np.polyfit(x1, y1, 1)
p1 = np.poly1d(z1)
b1 = p1(x)
ax1.plot(x, b1, 'r--')

z2 = np.polyfit(x1, y2, 1)
p2 = np.poly1d(z2)
b2 = p2(x)
ax1.plot(x, b2, 'b--')

z3 = np.polyfit(x1, y3, 1)
p3 = np.poly1d(z3)
b3 = p3(x)
ax1.plot(x, b3, 'g--')

z4 = np.polyfit(x1, y4, 1)
p4 = np.poly1d(z4)
b4 = p4(x)
ax1.plot(x, b4, 'k--')

ax1.set_xlim([0,9])
ax1.set_ylim([0,1300])

ax1.scatter(x1, y1, marker = '.')
ax1.errorbar(x1, y1, yerr = 0.1, xerr = 0, color = 'r', linestyle = 'None')

ax1.scatter(x1, y2, marker = '.')
ax1.errorbar(x1, y2, yerr = 0.1, xerr = 0, color = 'b', linestyle = 'None')

ax1.scatter(x1, y3, marker = '.')
ax1.errorbar(x1, y3, yerr = 0.1, xerr = 0, color = 'g', linestyle = 'None')

ax1.scatter(x1, y4, marker = '.')
ax1.errorbar(x1, y4, yerr = 0.1, xerr = 0, color = 'k', linestyle = 'None')

plt.title('График зависимости частоты от номера гармоники', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('n')
plt.ylabel('v, Гц')

ax1.grid()

plt.show()

print(z1, p1)
print(z2, p2)
print(z3, p3)
print(z4, p4)

x11 = np.array(x1)
y11 = np.array(y1)
y12 = np.array(y2)
y13 = np.array(y3)
y14 = np.array(y4)

x_mean = np.mean(x11**2)
y_mean1 = np.mean(y11**2)
y_mean2 = np.mean(y12**2)
y_mean3 = np.mean(y13**2)
y_mean4 = np.mean(y14**2)

xy_mean1 = np.mean(x11*y11)
xy_mean2 = np.mean(x11*y12)
xy_mean3 = np.mean(x11*y13)
xy_mean4 = np.mean(x11*y14)
k1 = xy_mean1/x_mean
k2 = xy_mean2/x_mean
k3 = xy_mean3/x_mean
k4 = xy_mean4/x_mean

print(k1, k2, k3, k4)

sk1 = (1/(len(x1)-1)*(y_mean1/x_mean - k1**2))**0.5
sk2 = (1/(len(x1)-1)*(y_mean2/x_mean - k2**2))**0.5
sk3 = (1/(len(x1)-1)*(y_mean3/x_mean - k3**2))**0.5
sk4 = (1/(len(x1)-1)*(y_mean4/x_mean - k4**2))**0.5

print(sk1, sk2, sk3, sk4)