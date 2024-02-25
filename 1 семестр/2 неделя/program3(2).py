st = input()
L = len(st)
nums_steps = L//2

symmetric_letters = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
mirror_letters = ['E', '3', 'J', 'L', 'S', '2', 'Z', '5']

flag1 = True
for i in range(nums_steps):
    if st[i] != st[-(i+1)]:
        flag1 = False
        break

flag2 = True
for i in range(nums_steps):
    if st[i] == 'E' and st[-(i+1)] == '3':
        if st[i] == 'J' and st[-(i+1)] == 'L':
            if st[i] == 'S' and st[-(i+1)] == '2':
                if st[i] == 'Z' and st[-(i+1)] == '5':
                    continue
                else:
                    flag2 = False

flag3 = True
for i in range(nums_steps):
    flag4 = False
    for j in range(len(symmetric_letters)):
        if st[i] == st[-(i + 1)]:
            if symmetric_letters[j] == st[i]:
                flag4 = True
            else:
                continue
        else:
            flag3 = False
    if flag4 == False:
        flag3 = False

if L % 2 == 1:
    if st[L//2] not in symmetric_letters:
        flag3 = False
        flag2 = False
    else:
        pass
res = f'{st} palindrome = {flag1}, mirrored = {flag2 or flag3}'
print(res)