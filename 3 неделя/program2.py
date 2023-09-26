N = int(input())
dividers = []
i = 2

while i <= N:
    if N % i == 0:
        N = N // i
        dividers.append(i)
        i -= 1
    i += 1
print(dividers)