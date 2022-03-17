a, b = input().split()
result = ''
length = max(len(a), len(b))
a = a.zfill(length)
b = b.zfill(length)
for i in range(length):
    result += str(int(a[i]) + int(b[i]))
print(result)
