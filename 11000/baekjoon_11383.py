n, m = map(int, input().split())
s1 = []
s2 = []
true = ''
for i in range(n):
    s1.append(input())
for i in range(n):
    s2.append(input())
for i in range(n):
    word = ''
    for j in range(m):
        word += (s1[i])[j] * 2
    if word != s2[i]:
        true = 'Not '
        break
print(true + 'Eyfa')
