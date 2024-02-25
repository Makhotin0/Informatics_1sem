A = list(map(int, input().split()))
L = len(A)

for i in range(len(A)):
    flag = True
    for j in range(len(A)):
        if A[i] == A[j] and i != j:
            flag = False
        else:
            continue
    if flag == True:
        print(A[i])
    else:
        continue
