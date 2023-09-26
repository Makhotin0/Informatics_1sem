st = input()
L = len(st)
nums_steps = L//2

flag = True
for i in range(nums_steps):
    if st[i] != st[-(i+1)]:
        flag = False
        break
res = f'{st} palindrome = {flag}'
print(res)