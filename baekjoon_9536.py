for _ in range(int(input())):
    cry = input().split()
    while True:
        answer = input()
        if answer == 'what does the fox say?':
            break
        answer = answer.split()[2]
        while answer in cry:
            cry.remove(answer)
    print(' '.join(cry))
