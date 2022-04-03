for _ in range(int(input())):
    words = input().split()
    for i in range(len(words)):
        if len(words[i]) == 4:
            words[i] = '****'
    print(*words, end='\n\n')
