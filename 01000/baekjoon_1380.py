from sys import stdin
index = 0
while True:
    index += 1
    n = int(input())
    if n == 0:
        break
    confiscate = []
    students = [stdin.readline().rstrip() for _ in range(n)]
    for _ in range(2 * n - 1):
        a, b = input().split()
        if a in confiscate:
            confiscate.remove(a)
        else:
            confiscate.append(a)
    print(f'{index} {students[int(confiscate[0]) - 1]}')
