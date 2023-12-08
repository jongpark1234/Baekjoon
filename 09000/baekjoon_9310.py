while True:
    n = int(input())
    if n == 0:
        break
    a1, a2, a3 = map(int, input().split())
    if a2 - a1 == a3 - a2:
        print(n * (2 * a1 + (n - 1) * (a2 - a1)) // 2)
    else:
        print(a1 * ((a2 // a1) ** n - 1) // (a2 // a1 - 1))
