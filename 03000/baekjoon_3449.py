for _ in range(int(input())):
    distance = 0
    a = input()
    b = input()
    for i in range(len(a)): 
        if a[i] != b[i]:
            distance += 1
    print(f'Hamming distance is {distance}.')
