while (n := input()) != '0':
    while int(n) > 9:
        temp = 0
        for i in n:
            temp += int(i)
        n = str(temp)
    print(n)
