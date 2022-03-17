def add(str):
    temp = 0
    for i in str:
        if i.isdigit():
            temp += int(i)
    return temp
print('\n'.join(sorted([input() for i in range(int(input()))], key = lambda x : (len(x), add(x), x))))
