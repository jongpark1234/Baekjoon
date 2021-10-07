h, m = map(int, input().split())
m = m - 45
if (m < 0):
    if (h - 1 < 0): 
        h = 23
    else: 
        h = h - 1
    m = m + 60
print(h, m)