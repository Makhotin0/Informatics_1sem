def fib(N, fibs):
    if N == 1:
        fibs[0] = 0
        return 0
    if N == 2:
        fibs[1] = 1
        return 1
    if fibs[N-1] != 0:
        return fibs[N-1]

    fibs[N-1] = fib(N-1, fibs) + fib(N-2, fibs)
    print(fibs)
    return fibs[N-1]

N = 10
fibs = [0 for i in range(N)]
print(fib(N, fibs))