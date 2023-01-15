numdict = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}
for _ in range(int(input())):
    s, x = input().split()
    numdict[s] += int(x)
print('YES' if 5 in numdict.values() else 'NO')
