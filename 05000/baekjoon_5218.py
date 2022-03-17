for i in range(int(input())):
    a, b = input().split()
    distance = []
    for i in range(len(a)):
        if a[i] > b[i]:
            distance.append(26 + ((ord(b[i]) - 64) - (ord(a[i]) - 64)))
        else:
            distance.append(ord(b[i]) - ord(a[i]))
    print('Distances:', ' '.join(map(str, distance)))
