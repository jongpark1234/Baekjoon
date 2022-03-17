n = int(input())
dot = 5
level = 7
for i in range(1, n):
    dot += level
    level += 3
print(dot % 45678)
