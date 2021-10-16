import sys
second = 0
for i in range(4):
    second += int(sys.stdin.readline())

print(str(second // 60) + "\n" + str(second % 60))