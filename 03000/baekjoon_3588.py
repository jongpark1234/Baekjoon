for i in range(int(input())):
    result = 0
    n = int(input())
    S, F = map(int, input().split())
    for j in range(n):
        s, f, r = map(int, input().split())
        for k in range(s, f + 1):
            if S <= k <= F:
                result += r
    print(f'Data Set {i + 1}:\n{result}\n')
