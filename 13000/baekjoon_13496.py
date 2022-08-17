for i in range(int(input())):
    result = 0
    n, s, d = map(int, input().split())
    for j in range(n):
        di, v = map(int, input().split())
        if s * d >= di:
            result += v
    print(f'Data Set {i + 1}:\n{result}\n')
