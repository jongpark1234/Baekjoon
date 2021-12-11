n, m = map(int, input().split())
sequence = []
def dfs(s):
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(s, n + 1):
        if i not in sequence:
            sequence.append(i)
            dfs(i + 1)
            sequence.pop()
dfs(1)
