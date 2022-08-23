n = int(input())
l = s = result = 0
for i in input():
    if i == 'L':
        l += 1
    elif i == 'S':
        s += 1
    elif i == 'R':
        if l:
            l -= 1
            result += 1
        else:
            break
    elif i == 'K':
        if s:
            s -= 1
            result += 1
        else:
            break
    else:
        result += 1
print(result)
