while True:
    try:
        idx = 0
        s, t = input().split()
        for i in t:
            if idx == len(s):
                break
            if i == s[idx]:
                idx += 1
        if idx == len(s):
            print('Yes')
        else:
            print('No')
    except EOFError:
        break
