for _ in range(int(input())):
    n = int(input())
    print(1 if n == 2 else min(n >> 1, sum(map(lambda x: int(x) > 1, input().split()))))
