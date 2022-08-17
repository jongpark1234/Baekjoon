for i in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print(f'Case #{i + 1}:', 'invalid!' if a + b <= c else 'equilateral' if a == b == c else 'isosceles' if a == b or b == c else 'scalene')
