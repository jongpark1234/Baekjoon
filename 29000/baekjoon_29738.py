for t in range(int(input())):
    x = int(input())
    print(f'Case #{t + 1}: {"Round 1" if x > 4500 else "Round 2" if x > 1000 else "Round 3" if x > 25 else "World Finals"}')
