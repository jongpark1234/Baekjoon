from math import gcd
idx = 0
numlist1 = [0 for _ in range(1000001)]
numlist2 = [0 for _ in range(1000001)]
a, b = map(int, input().split())
c = gcd(a, b)
a //= c
b //= c
while a != 1 or b != 1:
    while ~a & 1:
        idx += 1
        numlist1[idx] = 2
        numlist2[idx] = 2
        a >>= 1
    while ~b & 1:
        idx += 1
        numlist1[idx] = 1
        numlist2[idx] = 1
        b >>= 1
    if a < b:
        idx += 1
        numlist1[idx] = 2
        numlist2[idx] = 1
        idx += 1
        numlist1[idx] = 1
        numlist2[idx] = 1
        b = a + b >> 1
    if b < a:
        idx += 1
        numlist1[idx] = 1
        numlist2[idx] = 2
        idx += 1
        numlist1[idx] = 2
        numlist2[idx] = 2
        a = a + b >> 1
    c = gcd(a, b)
    a //= c
    b //= c
print(idx)
for i in range(1, idx + 1):
    print(('A' if numlist1[i] == 1 else 'B') + '+=' + ('A' if numlist2[i] == 1 else 'B'))
