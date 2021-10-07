a = int(input())
b = int(input())
c = list(map(int, str(b)))
for i in range(len(str(b))): print(a * c[len(c) - 1]), c.pop()
print(a * b)

