A = [0] * int(input())
for i in range(len(A)):
    A[i] = int(input())
    S = 1
for i in range(len(A)):
    S = i * A[i]
X = S ** (1 / len(A))
print(X)
