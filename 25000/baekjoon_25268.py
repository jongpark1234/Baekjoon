from random import choice
print(*[choice('aeiou').join(''.join(choice('bcdfghjklmnpqrstvwxyz') for _ in range(2)) for _ in range(5)) for _ in range(int(input()))])
