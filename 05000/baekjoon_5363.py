for _ in range(int(input())):
    speech = input().split()
    print(*speech[2:], *speech[:2])
