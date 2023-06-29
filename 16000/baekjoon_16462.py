n = int(input())
print(int(sum(min(int(input().replace('0', '9').replace('6', '9')), 100) for _ in range(n)) / n + 0.5))
