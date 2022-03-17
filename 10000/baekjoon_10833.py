rest = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    rest += b % a
print(rest)
