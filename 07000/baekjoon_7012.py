for i in range(int(input())):
    sm = [[0, 0, 0] for _ in range(1001)]
    n = int(input())
    b = sorted(list(map(int, input().split())), reverse = True)
    result = 0
    for j in range(1, n // 3 + 1)[::-1]:
        for k in range(j):
            sm[k][0] = b[k]
        mid, top, k = 0, 0, j
        while k < n and mid < j:
            if sm[mid][0] * 2 >= b[k] * 3:
                sm[mid][1] = b[k]
                mid += 1
            k += 1
        if mid < j or n - k < j:
            continue
        while k < n and top < j:
            if sm[top][1] * 2 >= b[k] * 3:
                top += 1
            k += 1
        if top == j:
            result = j
            break
    print(f'Data Set {i + 1}:\n{result}\n')
