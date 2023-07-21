n, k, p = map(int, input().split())
bread = list(map(int, input().split()))
print(sum(bread[i * k:(i + 1) * k].count(0) < p for i in range(n)))
