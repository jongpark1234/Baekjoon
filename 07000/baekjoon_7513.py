for i in range(int(input())):
    print(f'Scenario #{i + 1}:')
    a = int(input())
    word = [input() for _ in range(a)]
    for j in range(int(input())):
        temp = ''
        for i in list(map(int, input().split()))[1:]:
            temp += word[i]
        print(temp)
    print()
