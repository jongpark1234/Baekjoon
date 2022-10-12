for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    print(max(x) - min(x) << 1)
