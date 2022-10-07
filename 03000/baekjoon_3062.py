for _ in range(int(input())):
    n = input()
    temp = str(int(n) + int(n[::-1]))
    print('YES' if temp == temp[::-1] else 'NO')
