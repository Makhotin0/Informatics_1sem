def tri(N, i, k, j):
    if N == 0:
        return
    print(j*i)
    tri(N-1,i+1, k, j)
    if k % 2 == 1:
        print(j*(i-1))
    else:
        print(j*i)
k = int(input())
j = input()
N = k
if N % 2 == 1:
    tri(N//2 + 1,1, k, j)
else:
    tri(N//2, 1, k, j)