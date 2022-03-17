import sys
n = int(sys.stdin.readline())
num = 1
cnt = 0
for i in range(1, n + 1):
    num *= i
for i in str(num)[::-1]:
    if i != '0':
        break
    cnt += 1
print(cnt)
