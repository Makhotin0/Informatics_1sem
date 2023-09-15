A = [0] * int(input())
for i in range(len(A)):
    A[i] = int(input())
for i in A:
    S = A * i
X = S ** (1/len(A))
print(X)
#?????