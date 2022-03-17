a, b = input().split()
def crosswording(o1, o2):
    for i in range(o2):
        print('.' * o1 + b[i] + '.' * (len(a) - o1 - 1))
    print(a)
    for i in range(o2 + 1, len(b)):
        print('.' * o1 + b[i] + '.' * (len(a) - o1 - 1))
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            crosswording(i, j)
            exit(0)
