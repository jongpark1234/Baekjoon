p = 100 - int(input())
for i in [25, 10, 5, 1]:
    t, p = divmod(p, i)
    print(t, end=' ')
