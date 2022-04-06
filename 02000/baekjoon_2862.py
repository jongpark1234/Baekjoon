fibonacci = [0, 1]
for i in range(2, 80):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
n = int(input())
while True:
    c = n
    for i in range(1, 80):
        if c < fibonacci[i]:
            c = fibonacci[i - 1]
            break
    if c == n:
        break
    n -= c
print(n)
