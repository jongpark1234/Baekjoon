for _ in range(int(input())):
    consonant = 0
    vowel = 0
    for i in input():
        if i == ' ':
            pass
        elif i in 'AEIOUaeiou':
            vowel += 1
        else:
            consonant += 1
    print(consonant, vowel)
