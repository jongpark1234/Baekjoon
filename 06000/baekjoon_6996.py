for _ in range(int(input())):
    NOT = ''
    a, b = input().split()
    x = list(a); y = list(b)
    x.sort(); y.sort()
    if x != y:
        NOT = 'NOT '
    print(f'{a} & {b} are {NOT}anagrams.')
