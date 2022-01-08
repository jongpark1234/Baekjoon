n, t = map(int, input().split())
works = list(map(int, input().split()))
time = 0
for i in range(n):
    time += works[i]
    if time > t:
        print(i)
        exit()
print(n)
