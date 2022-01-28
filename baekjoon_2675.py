for _ in range(int(input())):
    r, s = input().split()
    temp = ''
    for i in s:
        temp += i * int(r)
    print(temp)
