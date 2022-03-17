for _ in range(int(input())):
    s = list(bin(int(input()))[2:])
    s.reverse()
    for i in range(len(s)):
        if s[i] == '1':
            print(i, end=' ')
