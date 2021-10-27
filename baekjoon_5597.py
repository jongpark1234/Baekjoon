import sys
students = [x for x in range(1, 31)]
for _ in range(28):
    del students[(students.index(int(sys.stdin.readline())))]
print(min(students), max(students), sep='\n')
