f = open("input.txt", 'r')
A = []
for line in f:
    A.append(line)
f.close()
g = open('output.txt', 'w')


#A[0] -- строка чисел, разделенных пробелами (str)
#A[1] -- знак арифм операции (str)
#A[2] -- основание системы сч. (str)

nums = list(map(int, A[0].split()))
c = int(A[2])
nums_dec = []j in range(len(num_str)): #каждое число переводим в десятичную
        num_dec += int(num_str[-(j + 1)]) * c ** j
    nums_dec.append(num_dec) #записываем
S = nums_dec
print(S)
#Шаг 2: просуммировать/перемножить числа в списке nums_dec
sum = 0
prod = 1
for i in range(len(S)):
    if A[1] == ' +' or '+':
        sum += S[i]
    elif A[1] == ' *' or '*':
        prod *= S[i]
    elif A[1] == ' -' or '-':
        sum -= S[i]
print(sum)
print(prod)

# Шаг 3: перевести результат в c-ичную систему счисления и записать в output
if A[1] == ' +' or A[1] == ' -' or A[1] == '+' or A[1] == '-':
x = sum
print(x)
A = []
while x != 0:
    A.append(x%c)
    x = x // c
ans = ''.join(map(str, A[::-1]))
g.write(str(ans))
g.close()
else:
    y = prod[i]
    B = []
    while y != 0:
        B.append(x%c)
        y = y // c
    ans = ''.join(map(str, B[::-1]))
    g.write(str(ans))
    g.close()
  #??????????