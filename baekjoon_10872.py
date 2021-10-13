import sys
n = int(sys.stdin.readline())
num = 1
for i in range(1, n + 1):
    num *= i
print(num)