for _ in range(int(input())):
    n = int(input())
    print('koosaga' if n & 1 and '1' not in bin(n - 1 >> 1)[2:][-2::-2] else 'cubelover')
