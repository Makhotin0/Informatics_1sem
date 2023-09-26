import numpy as np
M = int(input())
N = int(input())

A = [0 for i in range(N)]
B = []
for i in range(N):
    A = [0 for j in range(M)]
    B.append(A)
print(*B, sep = '\n')

count = 0
i, j, k = 0, -1, 1
while count < N*M:
    while j < M - k:
        count += 1
        j += 1
        B[i][j] += count
    if count >= M*N:
        break
    else:
        while i < N - k:
            count += 1
            i += 1
            B[i][j] += count
        if count >= M*N:
            break
        else:
            while j > k - 1:
                count += 1
                j -= 1
                B[i][j] += count
            if count >= M*N:
                break
            else:
                while i > k:
                    count += 1
                    i -= 1
                    B[i][j] += count
    k += 1

print(*B, sep = '\n')