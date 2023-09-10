n = input()
setN = set(map(int, n))
if setN <= {2, 0, 1, 8}:
    if setN == {2, 0, 1, 8}:
        if n.count('2') == n.count('0') == n.count('1') == n.count('8'):
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)
