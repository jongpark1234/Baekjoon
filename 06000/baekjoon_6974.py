for _ in range(int(input())):
    n = input()
    m = input()
    print(int(n) // int(m))
    print(int(n) % int(m.rjust(len(n), '0')))
    print()
