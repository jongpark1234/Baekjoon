for i in [*map(int, [*open(0)])]:
    numlist = [False for _ in range(10)]
    p = 10
    s = result = 0
    while p:
        s, result = s + i, result + 1
        q = s
        while q:
            q, r = divmod(q, 10)
            if not numlist[r]:
                numlist[r] = True
                p -= 1
                if not p:
                    break
    print(result)
