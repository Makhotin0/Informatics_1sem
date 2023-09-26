s = input().split()
#3 ABCCDF, s = ['3', 'ABCCDF']
G = int(s[0])
st = s[1]

L = len(st)
num = L//G
print(num)

A = []
for i in range(num):
    A.append(st[i*G:(i+1)*G])

print(A)

B = []
for j in range(len(A)):
    B.append(A[j][::-1])
print(B)

res = ''.join(B)
print(res)