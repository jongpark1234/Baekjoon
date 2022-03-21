n = int(input())
fibonacci = [0, 1]
for i in range(2, abs(n) + 1):
    fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % 1000000000)
print(-1 if n < 0 and n % 2 == 0 else 0 if n == 0 else 1)
print(fibonacci[abs(n)])
