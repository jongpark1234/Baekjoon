fence = [0 for _ in range(101)]
a, b = map(int, input().split())
c, d = map(int, input().split())
for i in range(a, b):
    fence[i] = 1
for i in range(c, d):
    fence[i] = 1
print(sum(fence))
