for _ in range(int(input())):
    n = int(input())
    print('TAK' if n % 9 == 0 or n % 3 == 2 else 'NIE')
