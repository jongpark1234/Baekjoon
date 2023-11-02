n = int(input())
a = list(map(int, input().split()))
print(2, int(sum(map(lambda x: x % 2, a)) > len(a) // 2))
