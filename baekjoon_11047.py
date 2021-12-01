n, k = map(int, input().split()) 
coinlist = [int(input()) for _ in range(n)]
count = 0
for i in reversed(range(n)):
    count += k // coinlist[i]
    k %= coinlist[i]
print(count)
