result = 0
n = int(input())
a = sorted(map(int, input().split()))
while a:
    result += 1
    for i in range(1, (len(a) > 1) + 2):
        a[-i] -= 1
    for i in range(a.count(0)):
        a.remove(0)
    a = sorted(a)
print(-1 if result > 1440 else result)
