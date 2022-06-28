for i in range(int(input())):
    n = result = int(input())
    a = sorted(list(map(int, input().split())))
    for j in range(n):
        if a[j] > j:
            result = j
            break
    print(f'Data Set {i + 1}:\n{result}\n')
