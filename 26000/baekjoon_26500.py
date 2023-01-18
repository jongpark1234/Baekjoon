for _ in range(int(input())):
    a, b = sorted(map(float, input().split()))
    print(f'{b - a:.1f}')
