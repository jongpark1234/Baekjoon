k = int(input())
a = [1, 0]
b = [0, 1]
for i in range(2, k + 1):
    a.append(a[i - 2] + a[i - 1])
    b.append(b[i - 2] + b[i - 1])
print(a[-1], b[-1])
