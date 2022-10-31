n = int(input())
cnt = prev = 0
for i in range(1, 1000):
    prev = cnt
    cnt += i
    if cnt >= n:
        break
mole, deno = i, 1
for i in range(n - prev - 1):
    mole -= 1
    deno += 1
print(mole, deno)
