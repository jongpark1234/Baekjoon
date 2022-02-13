lines = sorted(list(map(int, input().split())))
print(lines[0] + lines[1] + min(lines[2], lines[0] + lines[1] - 1))
