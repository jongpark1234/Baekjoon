for _ in range(int(input())):
    print(sum(max(max(map(int, input().split())), 0) for _ in range(int(input()))))
