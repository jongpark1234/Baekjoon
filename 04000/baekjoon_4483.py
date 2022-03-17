for i in range(int(input())):
    namelist = [input() for _ in range(int(input()))]
    presentList = []
    for _ in range(int(input())):
        presentList += input().split()
    print(f'Test set {i + 1}:')
    for j in namelist:
        print(f'{j} is present' if j in presentList else f'{j} is absent')
    print()
