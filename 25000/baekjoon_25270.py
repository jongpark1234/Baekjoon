n = int(input())
l = h = 0
while not str(n - l).endswith('99'):
    l += 1
while not str(n + h).endswith('99'):
    h += 1
print(n - l if l < h else n + h)
