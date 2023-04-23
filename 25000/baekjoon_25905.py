print(__import__('math').prod(p / (i + 1) for i, p in enumerate(sorted([float(input()) for _ in range(10)])[1:])) * 1000000000)
