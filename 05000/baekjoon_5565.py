import sys
total = int(sys.stdin.readline())
sum = 0
for _ in range(9):
    sum += int(sys.stdin.readline())
print(total - sum)
