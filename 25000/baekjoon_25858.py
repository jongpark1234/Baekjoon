n, d = map(int, input().split())
amounts = [int(input()) for _ in range(n)]
Sum = sum(amounts)
for i in amounts:
    print(d // Sum * i)
