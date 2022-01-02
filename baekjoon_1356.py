n = input()
for i in range(1, len(n)):
    num1, num2 = n[:i], n[i:]
    front, back = 1, 1
    for j in num1:
        front *= int(j)
    for j in num2:
        back *= int(j)
    if front == back:
        print('YES')
        exit(0)
print('NO')
