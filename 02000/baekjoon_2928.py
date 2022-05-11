result = [0 for _ in range(1000005)]
time = [0 for _ in range(1000005)]
def store(s, e):
    if s < 0:
        s, e = e, s
    result[abs(s)] += 1
    result[abs(e) + 1] -= 1
def search(x1, x2, y1, y2):
    if x1 <= 0 <= x2:
        search(x1, -1, y1, y2)
        search(1, x2, y1, y2)
        store(y1, y2)
        return
    if y1 <= 0 <= y2:
        search(x1, x2, y1, -1)
        search(x1, x2, 1, y2)
        store(x1, x2)
        return
    if x1 < 0 and x2 < 0:
        x1, x2 = -x2, -x1
    if y1 < 0 and y2 < 0:
        y1, y2 = -y2, -y1
    if max(x1, y1) <= min(x2, y2):
        result[max(x1, y1)] += (max(x1, y1) - x1 + 1) * (max(x1, y1) - y1 + 1)
        result[min(x2, y2) + 1] -= (max(x1, y1) - x1 + 1) * (max(x1, y1) - y1 + 1)
        time[max(x1, y1) + 1] += 2
        time[min(x2, y2) + 1] -= 2
        result[min(x2, y2) + 1] -= (min(x2, y2) - max(x1, y1)) * 2
    if max(max(x1, y1), min(x2, y2) + 1) <= max(x2, y2):
        if x2 < y2:
            result[max(max(x1, y1), min(x2, y2) + 1)] += x2 - x1 + 1
            result[max(x2, y2) + 1] -= x2 - x1 + 1
        else:
            result[max(max(x1, y1), min(x2, y2) + 1)] += y2 - y1 + 1
            result[max(x2, y2) + 1] -= y2 - y1 + 1
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    search(x1, x2, y1, y2)
for i in range(1, 1000001):
    time[i] += time[i - 1]
    result[i] += time[i]
for i in range(2):
    for j in range(1, 1000001):
        result[j] += result[j - 1]
m = int(input())
for i in map(int, input().split()):
    print(result[i])
