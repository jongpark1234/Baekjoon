n = N = int(input())
fibonacci = [0, 1]
for i in range(2, 32):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
while True:
    temp = n
    for i in range(1, 32):
        if temp < fibonacci[i]:
            temp = fibonacci[i - 1]
            break
    if temp == n:
        break
    n -= temp
print([n, -1][n == N])
