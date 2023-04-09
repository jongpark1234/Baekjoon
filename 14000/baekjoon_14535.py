tc = 0
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    graph = [0 for _ in range(12)]
    for _ in range(n):
        d, m, y = map(int, input().split())
        graph[m - 1] += 1
    print(f'Case #{tc}:')
    for i in range(12):
        print(f'{month[i]}:{"*" * graph[i]}')
