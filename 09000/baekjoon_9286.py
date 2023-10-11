from sys import stdin
for x in range(int(stdin.readline())):
    print(f'Case {x + 1}:')
    for _ in range(int(stdin.readline())):
        grade = int(stdin.readline())
        if grade < 6:
            print(grade + 1)
