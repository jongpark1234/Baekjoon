from collections import Counter
for _ in range(int(input())):
    a = input()
    a = a.replace(' ', '')
    A = Counter(a).most_common()
    try:
        if A[0][1] == A[1][1]:
            print('?')
        else:
            print(A[0][0])
    except IndexError:
        print(A[0][0])
