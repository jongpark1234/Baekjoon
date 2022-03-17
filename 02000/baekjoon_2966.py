n = int(input())
s = input()
count = [0, 0, 0]
cycle = [['A', 'B', 'C'], ['B', 'A', 'B', 'C'], ['C', 'C', 'A', 'A', 'B', 'B']]
for i in range(n):
    if cycle[0][i % 3] == s[i]:
        count[0] += 1
for i in range(n):
    if cycle[1][i % 4] == s[i]:
        count[1] += 1
for i in range(n):
    if cycle[2][i % 6] == s[i]:
        count[2] += 1
print(max(count))
for i in range(3):
    if count[i] == max(count):
        if i == 0:
            print('Adrian')
        elif i == 1:
            print('Bruno')
        else:
            print('Goran')
