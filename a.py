numlist = []
x = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    numlist.append(a * b)
print(['No', 'Yes'][sum(numlist) == x])
