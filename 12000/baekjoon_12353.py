from sys import stdin
from math import ceil, floor
def feet(n):
    return f'{n // 12}\'{n % 12}"'
for i in range(int(stdin.readline())):
    gender, mother, father = stdin.readline().rstrip().split()
    mother = int(mother.split('\'')[0]) * 12 + int(mother.split('\'')[1][:-1])
    father = int(father.split('\'')[0]) * 12 + int(father.split('\'')[1][:-1])
    tall = mother + father + 5 if gender == 'B' else mother + father - 5
    print(f'Case #{i + 1}:', feet(ceil(tall / 2) - 4), 'to', feet(floor(tall / 2) + 4))
