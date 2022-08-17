for _ in range(int(input())):
    input()
    n = int(input())
    candy = sum(int(input()) for _ in range(n))
    print('YES' if candy % n == 0 else 'NO')
