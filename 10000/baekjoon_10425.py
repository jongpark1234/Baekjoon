fiboMap = { 0: 0, 1: 1 }
a, b = 0, 1
for i in range(2, 100001):
    a, b = b, a + b
    fiboMap[b] = i
for i in [*open(0)][1:]:
    print(fiboMap[int(i)])
