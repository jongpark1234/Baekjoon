n, k = map(int, input().split())
error = True
for i in range(1, n + 1):
    if not n % i:
        k -= 1
        if k == 0:
            error = False
            print(i)
if error:
    print(0)
