class Vector():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        #не знаю как сделать assert :(

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(other - self.x, other - self.y, other - self.z)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'

def center(Vectors):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    for i in range (len(Vectors)):
        sum_x += Vectors[i].x
        sum_y += Vectors[i].y
        sum_z += Vectors[i].z
    x_center = sum_x / len(Vectors)
    y_center = sum_y / len(Vectors)
    z_center = sum_z / len(Vectors)
    return f'Координаты центра масс: x = {x_center} y = {y_center} z = {z_center}'

def square(Vectors):
    S_max = 0
    for i in range(len(Vectors)):
        for j in range(i + 1, len(Vectors)):
            for k in range(j + 1, len(Vectors)):
                v1 = Vectors[j] - Vectors[i]
                v2 = Vectors[k] - Vectors[i]
                v1v2 = Vector(v1.y * v2.z - v2.y * v1.z, v1.x * v2.z - v2.x * v1.z, v1.x * v2.y - v2.x * v1.y)
                S = 0.5 * v1v2.__abs__()
                S_max = max(S_max, S)
    return S_max

Vectors = []
N = int(input())
for i in range(N):
    s = list(input().split())
    V = Vector(s[0], s[1], s[2])
    Vectors.append(V)

#print(Vectors[1].__str__())
#print(Vectors[0] * Vectors[2] + 2)

#Координата центра масс
print(center(Vectors))

#Максимальная площадь
print(square(Vectors))

