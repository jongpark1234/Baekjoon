for _ in range(int(input())):
    result = 0
    n, k = map(int, input().split())
    for i in map(int, input().split()):
        result += i // k
    print(result)
