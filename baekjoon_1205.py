n, m, p = map(int, input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    if n == p and m <= arr[-1]:
        print(-1)
    else:
        for i in range(n):
            if m >= arr[i]:
                print(i + 1)
                break
        else:
            print(n + 1)
