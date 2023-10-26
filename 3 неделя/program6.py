import numpy as np
tx = [1,2,3,4,5]
ty = [2*i + 1 for i in tx]
x = np.array(tx)
y = np.array(ty)

print(x,y)

x_mean = np.mean(x)
y_mean = np.mean(y)

x_mean1 = np.mean(x**2)
y_mean1 = np.mean(y**2)

numerator = (x - x_mean)*y_mean
denominator = x_mean1 - x_mean**2
a = np.sum(numerator)/np.sum(denominator)
print(a)
b = y_mean - a*x_mean
print(b)

Dx = x_mean1 - x_mean**2
Dy = y_mean1 - y_mean**2

Sk = (1/(len(tx)-2)*(Dy/Dx - a**2))**0.5
Sb = Sk * (x_mean1)**0.5

print(Sk)
print(Sb)
