n, a, b = map(int, input().split())
piles = list(map(int, input().split()))
minNum = min(a, b)
k = 0
B = 0
N = 0
for i in range(n):
    k ^= (piles[i] % (minNum + 1))
    if piles[i] > minNum:
        N = piles[i]
        B += 1
if B == 0 or a == b:
    print('Petyr' if k else 'Varys')
elif B == 1 and minNum == a:
    value = k ^ (N % (a + 1))
    temp = a + 1
    d = (((N - value) % temp) + temp) % temp
    print('Varys' if d <= 0 or d > a or N - d > a else 'Varys' if value != (N - d) % temp else 'Petyr')
else:
    print('Varys' if a < b else 'Petyr')
