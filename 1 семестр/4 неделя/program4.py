import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris-data.csv')
A = list((df['SepalLengthCm']))
B = list((df['PetalLengthCm']))
C = list((df['SepalWidthCm']))
D = list((df['PetalWidthCm']))

dots1 = []
dots2 = []
for i in range(len(A)):
    a = A[i]
    c = C[i]
    b = B[i]
    d = D[i]
    dots1.append((c,a))
    dots2.append((d,b))

dots1.sort()
dots2.sort()

A1 = []
B1 = []
C1 = []
D1 = []
for i in range(len(A)):
    A1.append(dots1[i][1])
    C1.append(dots1[i][0])
    B1.append(dots2[i][1])
    D1.append(dots2[i][0])

print(A1)
print(B1)
print(C1)
print(D1)

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

x = [0, 7]
a = [0, 2]

z = np.polyfit(C1, A1, 1)
print(z)
p = np.poly1d(z)
print(p(x))
y1 = p(x)
z1 = np.polyfit(D1, B1, 1)
p1 = np.poly1d(z1)
b1 = p1(x)
ax1.plot(x, y1, 'r')
ax2.plot(x, b1,'b')

ax1.set_xlim([0,6])
ax1.set_ylim([3,8])
ax2.set_xlim([0,3])
ax2.set_ylim([0,8])

ax1.scatter(C1,A1, marker = '.')
ax2.scatter(D1,B1, marker = '.')

ax1.grid()
ax2.grid()

plt.show()

#сайпай фит
