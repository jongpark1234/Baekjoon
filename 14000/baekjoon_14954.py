numlist = []
n = input()
while n != '1':
    temp = 0
    numlist.append(n)
    for i in n:
        temp += int(i) ** 2
    n = str(temp)
    if n in numlist:
        print('UNHAPPY')
        break
else:
    print('HAPPY')
