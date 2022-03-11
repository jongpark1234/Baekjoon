n = int(input())
time = 0
k = 0
while n != 0:
    k += 1
    if n < k:
        k = 1
    time += 1
    n -= k
print(time)
