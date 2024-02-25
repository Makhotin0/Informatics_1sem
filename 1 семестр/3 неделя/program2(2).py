N = int(input())

def div(N):
    i = 2
    while i <= N:
        if N % i == 0:
            N = N // i
            print(i)
            i -= 1
        i += 1

div(N)