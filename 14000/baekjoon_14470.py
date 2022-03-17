import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
time = 0
while a < 0:
    a += 1
    time += c
if a == 0:
    time += d
while a < b:
    a += 1
    time += e
print(time)