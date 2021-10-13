def rev(n):
    temp = ''
    for i in range(len(n)):
        temp += n[i]
    return int(temp)
x, y = map(str, input().split())
x, y = list(x), list(y)
x.reverse(), y.reverse()
t = list(map(str, str(rev(x) + rev(y))))
t.reverse()
print(rev(t))