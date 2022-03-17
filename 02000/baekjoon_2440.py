n = int(input())
temp = n
for i in range(n):
    for j in range(temp):
        print('*', end="")
    temp -= 1
    print()
