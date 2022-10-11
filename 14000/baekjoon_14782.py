n = int(input())
print(sum(i for i in range(1, n + 1) if not n % i))
