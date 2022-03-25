for i in range(int(input())):
    n, m = map(int, input().split())
    dis = m - n
    print(f'Scenario #{i + 1}:\n{((dis * (dis + 1)) // 2) + (n * (dis + 1))}\n')
