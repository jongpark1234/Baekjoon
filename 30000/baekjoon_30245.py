print(-1 if __import__('math').gcd(n := int(input()), 6) != 1 else ' '.join(map(str, [i * 2 % n + 1 for i in range(1, n + 1)])))
