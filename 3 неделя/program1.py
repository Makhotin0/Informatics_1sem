def fib(N, depth = 0):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    print(depth)

    res = fib(N-1, depth+1) + fib(N-2, depth+1)

    print(f'on step {depth} fib = {res}')

    return res

print(fib(8))