while True:
    n = int(input())
    if n == 0:
        break
    mary = list(map(int, input().split())).count(0)
    print(f'Mary won {mary} times and John won {n - mary} times')
