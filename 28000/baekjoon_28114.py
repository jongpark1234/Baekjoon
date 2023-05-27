team = [input().split() for _ in range(3)]
print(''.join(map(lambda x: str(int(x[1]) % 100), sorted(team, key=lambda x: int(x[1]) % 100))))
print(''.join(map(lambda x: x[2][0], sorted(team, key=lambda x: -int(x[0])))))
