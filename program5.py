N = input()
b = int(input())
c = int(input())

N_dec = 0
for i in range(len(N)):
    N_dec += int(N[-(i+1)]) * b ** i

print(N_dec)

x = N_dec
A = []
while x != 0:
    A.append(x%c)
    x = x // c

ans = ''.join(map(str, A[::-1]))
print(ans)
