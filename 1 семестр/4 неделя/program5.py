import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

df = pd.read_csv('BTC_data.csv')
A = list((df['close']))
Bo = list((df['time']))

B = []
for i in range(len(Bo)):
    S = Bo[i]
    B.append(S[0:10])

print(B)

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(111)

df = pd.DataFrame({'date': np.array([datetime.datetime(int(B[i][0:4]), int(B[i][5:7]), int(B[i][8:10])) for i in range(len(B))]), 'sales': A})

ax1.plot(df.date, df.sales, linewidth = 1)

plt.xticks(rotation=10, ha='right')

plt.title('Цена биткоина')

plt.xlabel('Дата')
plt.ylabel('Цена')

plt.show()

#Сколько не пытался, не получается аппроксимировать цену биткоина. Мешает то, что у меня цена зависит от даты, которая не является числом.