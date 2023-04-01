q = int(input())
strlist = [input() for _ in range(q)]
for _ in range(int(input())):
    idx = int(input())
    print(f'Rule {idx}: {strlist[idx - 1] if q >= idx > 0 else "No such rule"}')
