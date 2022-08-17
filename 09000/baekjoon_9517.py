time = 0
k = int(input())
for i in range(int(input())):
    t, z = input().split()
    time += int(t)
    if time >= 210:
        print(k)
        break
    if z == 'T':
        k = max(1, (k + 1) % 9)
