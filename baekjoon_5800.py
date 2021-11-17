for i in range(int(input())):
    total = 0
    numlist = sorted(list(map(int, input().split()))[1:])
    for j in range(len(numlist) - 1):
        total = max(abs(numlist[j] - numlist[j + 1]), total)
    print(f'Class {i + 1}', f'Max {max(numlist)}, Min {min(numlist)}, Largest gap {max(numlist) - min(numlist)}', sep='\n')
