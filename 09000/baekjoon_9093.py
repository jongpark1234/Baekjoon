for _ in range(int(input())):
    s = list(map(list, input().split()))
    for i in s:
        print(''.join(i[::-1]), end=' ')
