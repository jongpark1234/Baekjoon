r, c = map(int, input().split())
rows = [int(input()) for _ in range(r - 1)]
columns = list(map(int, input().split()))
rows += [columns[0]]
print(rows.index(min(rows)) + 1, columns.index(min(columns)) + 1)
