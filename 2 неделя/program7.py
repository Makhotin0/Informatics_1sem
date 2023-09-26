A = list(map(int, input().split()))
N = 0
M = 0

for i in range(len(A)):
    count = 1
    for j in range(len(A)):
        if A[i] == A[j] and i != j:
            count += 1
        else:
            continue
    if N < count:
        N = count
        M = A[i]
    else:
        continue

print(M)


