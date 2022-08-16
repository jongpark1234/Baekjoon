a, b, c = map(int, input().split())
parking = [0 for _ in range(101)]
for _ in range(3):
    l, r = map(int, input().split())
    for i in range(l, r):
        parking[i] += 1
print(sum(map(lambda x: [0, a, b * 2, c * 3][x], parking)))
