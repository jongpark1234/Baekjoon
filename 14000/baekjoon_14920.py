c = int(input())
n = 1
while c != 1:
    n += 1
    c = c * 3 + 1 if c & 1 else c >> 1
print(n)
