polish_list = input().split()

def polish_cow(polish_list):
    start_len = len(polish_list)
    i = 0
    flag = True
    while i < len(polish_list):
        if polish_list[i] == '+':
            try:
                float(polish_list[i-2])
                float(polish_list[i-1])
            except:
                print('Неправильная запись')
                flag = False
                break
            plus = float(polish_list[i - 2]) + float(polish_list[i - 1])
            polish_list.pop(i)
            polish_list.pop(i - 1)
            polish_list.pop(i - 2)
            polish_list.insert(i - 2, plus)
            i -= 2
        elif polish_list[i] == '-':
            try:
                float(polish_list[i-2])
                float(polish_list[i-1])
            except:
                print('Неправильная запись')
                flag = False
                break
            minus = float(polish_list[i-2]) - float(polish_list[i-1])
            polish_list.pop(i)
            polish_list.pop(i-1)
            polish_list.pop(i-2)
            polish_list.insert(i - 2, minus)
            i -= 2
        elif polish_list[i] == '*':
            try:
                float(polish_list[i-2])
                float(polish_list[i-1])
            except:
                print('Неправильная запись')
                flag = False
                break
            mult = float(polish_list[i-2]) * float(polish_list[i-1])
            polish_list.pop(i)
            polish_list.pop(i-1)
            polish_list.pop(i-2)
            polish_list.insert(i - 2, mult)
            i -= 2
        elif polish_list[i] == '/':
            try:
                float(polish_list[i-2])
                float(polish_list[i-1])
                float(polish_list[i - 2]) / float(polish_list[i - 1])
            except:
                print('Неправильная запись')
                flag = False
                break
            divide = float(polish_list[i-2]) / float(polish_list[i-1])
            polish_list.pop(i)
            polish_list.pop(i-1)
            polish_list.pop(i-2)
            polish_list.insert(i - 2, divide)
            i -= 2
        i += 1

    if len(polish_list) == 1 and start_len != 1:
        print(polish_list[0])
    else:
        if flag == True:
            print('Неправильная запись')
    return

polish_cow(polish_list)