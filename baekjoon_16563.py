def factorize(n):
    temp = []
    while n > 1:
        temp.append(seive[n])
        n //= seive[n]
    return temp
MAX = 5000001
seive = [0] * MAX
seive[0], seive[1] = -1, -1
for i in range(2, MAX):
    seive[i] = i
for i in range(2, int(MAX ** 0.5) + 1):
    if seive[i] == i:
        for j in range(i * i, MAX, i):
            if seive[j] == j:
                seive[j] = i
t = int(input())
for i in list(map(int, input().split())):
    print(*factorize(i))
