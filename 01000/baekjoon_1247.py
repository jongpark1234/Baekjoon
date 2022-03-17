for i in range(3):
    Sum = sum([int(input()) for _ in range(int(input()))])
    print('+' if Sum > 0 else '-' if Sum < 0 else '0')
