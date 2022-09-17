from collections import deque
while True:
    result = 0
    while True:
        try:
            n, m = map(int, input().split())
            break
        except ValueError:
            continue    
    if n == m == 0:
        break
    numlist1 = [0 for _ in range(n)]
    numlist2 = [-1 for _ in range(n)]
    grundy = [set() for _ in range(n)]
    graph = [[] for _ in range(n)]
    Input = []
    while len(Input) != m << 1:
        Input.extend(list(map(int, input().split())))
    for i in range(0, m << 1, 2):
        graph[Input[i + 1]].append(Input[i])
        numlist1[Input[i]] += 1
    queue = deque([])
    for i in range(n):
        if numlist1[i] == 0:
            queue.append(i)
            numlist2[i] = 0
    while queue:
        cur = queue.popleft()
        if numlist2[cur] == -1:
            temp = 0
            while temp in grundy[cur]:
                temp += 1
            numlist2[cur] = temp
        for i in graph[cur]:
            grundy[i].add(numlist2[cur])
            numlist1[i] -= 1
            if numlist1[i] == 0:
                queue.append(i)
    Input = []
    while len(Input) != n:
        Input.extend(list(map(int, input().split())))
    for i in range(n):
        for _ in range(Input[i]):
            result ^= numlist2[i]
    print('First' if result else 'Second')
