n = int(input())
k = int(input())
if n > 60 + k:
    print(1500 * (60 + k) + 3000 * (n - (60 + k)))
else:
    print(1500 * n)
