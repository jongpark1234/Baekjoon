n, a, b = map(int, input().split())
piles = [int(input()) for _ in range(n)]
minNum = min(a, b)
k = B = N = 0
for i in range(n):
    k ^= (piles[i] % (minNum + 1))
    if piles[i] > minNum:
        N = piles[i]
        B += 1
if B == 0 or a == b:
    print('Hanako' if k else 'Jiro')
elif B == 1 and minNum == a:
    value = k ^ (N % (a + 1))
    temp = a + 1
    d = (((N - value) % temp) + temp) % temp
    print('Jiro' if d <= 0 or d > a or N - d > a else 'Jiro' if value != (N - d) % temp else 'Hanako')
else:
    print('Jiro' if a < b else 'Hanako')
