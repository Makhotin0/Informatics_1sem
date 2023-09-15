f = open('input.txt')
A = []
for line in f:
    A.append(line)
#A[0] -- строка чисел, разделённых пробелом (str)
#A[1] -- знак операции (str)
f.close()
g = open('output.txt', 'w')
S = list(map(int, A[0].split()))
sum = 0
prod = 1
for i in range(len(S)):
    if A[1] == '+':
        sum += S[i]
    elif A[1] == '*':
        prod *= S[i]
    elif A[1] == '-':
        sum -= S[i]
if A[1] == '+' or A == '-':
    g.write(str(sum))
if A[1] == '*':
    g.write(str(prod))
g.close()
    
    
    


