piclist = [''] + [input() for _ in range(int(input()))]
for _ in range(int(input())):
    l, r = map(int, input().split())
    print('\n'.join(piclist[l:r + 1]))
