fibonacci = [0, 1]
for i in range(2, 80):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
n = int(input())
while True:
    temp = n
    for i in range(1, 80):
        if temp < fibonacci[i]:
            temp = fibonacci[i - 1]
            break
    if temp == n:
        break
    n -= temp
print(n)
