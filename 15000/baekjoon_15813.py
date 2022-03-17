n = int(input())
s = input()
namescore = 0
for i in range(n):
    namescore += ord(s[i]) - 64
print(namescore)
