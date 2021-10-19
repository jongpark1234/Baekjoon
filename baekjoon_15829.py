m = 1234567891
l = int(input())
s = input()
temp = 0
for i in range(l):
    temp += (ord(s[i]) - 96) * (31 ** i)
print(temp % m)
