for _ in range(int(input())):
    m, a = input().split()
    print(*list(map(lambda x: chr(int(x) + 64) if a == 'N' else ord(x) - 64, input().split())))
