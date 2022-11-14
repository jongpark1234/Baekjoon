for _ in range(int(input())):
    result = 0
    missions = [list(map(int, input().split())) for _ in range(int(input()))]
    k, d, a = map(int, input().split())
    for i in missions:
        result += max(k * i[0] - d * i[1] + a * i[2], 0)
    print(result)
