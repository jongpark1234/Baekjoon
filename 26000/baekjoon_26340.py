for _ in range(int(input())):
    s1, s2, f = map(int, input().split())
    print(f'Data set: {s1} {s2} {f}')
    for _ in range(f):
        if s1 == s2 == 0:
            break
        if s1 >= s2:
            s1 >>= 1
        else:
            s2 >>= 1
    print(*sorted([s1, s2], reverse=True), end='\n\n')
