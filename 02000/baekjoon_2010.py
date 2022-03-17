from sys import stdin
result = 0
for _ in range(int(stdin.readline())):
    result += int(stdin.readline()) - 1
print(result + 1)
