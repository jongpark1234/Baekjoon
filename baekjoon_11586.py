n = int(input())
a = [input() for _ in range(n)]
p = int(input())
if p == 1:
    print('\n'.join(a))
elif p == 2:
    for i in a:
        print(i[::-1])
else:
    print('\n'.join(a[::-1]))
