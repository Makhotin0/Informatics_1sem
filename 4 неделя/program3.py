import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')
A = list((df['Species']))

B = A.count('Iris-setosa')
C = A.count('Iris-versicolor')
D = A.count('Iris-virginica')

E = list((df['PetalLengthCm']))

F = []
G = []
H = []

for i in range(len(E)):
    if E[i] < 1.2:
        F.append(E[i])
    elif E[i] >= 1.2 and E[i] <= 1.5:
        G.append(E[i])
    else:
        H.append(E[i])

fig = plt.figure(figsize = (16,9))
plt1 = fig.add_subplot(211)
plt2 = fig.add_subplot(212)

plt1.pie([B, C, D], labels = ['Iris-setosa','Iris-versicolor', 'Iris-virginica'])
plt2.pie([len(F), len(G), len(H)], labels = ['Меньше 1,2', 'Больше 1,2 и меньше 1,5', 'Больше 1,5'])

plt.show()