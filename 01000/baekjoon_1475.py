count = 0
s = list(input())
while s:
    count += 1
    for i in range(10):
        if i == 6:
            if '6' in s:
                s.remove('6')
            elif '9' in s:
                s.remove('9')
        elif i == 9:
            if '9' in s:
                s.remove('9')
            elif '6' in s:
                s.remove('6')
        else: 
            if str(i) in s:
                s.remove(str(i))
print(count)
