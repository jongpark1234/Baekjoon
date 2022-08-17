for _ in range(int(input())):
    n = int(input())
    print(sum(i * sum(i for i in range(1, i + 2)) for i in range(1, n + 1)))
