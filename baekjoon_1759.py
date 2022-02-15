from itertools import combinations
l, c = map(int, input().split())
for i in list(combinations(sorted(input().split()), l)):
    vowel = 0
    consonant = 0
    for j in i:
        if j in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    if vowel > 0 and consonant > 1:
        print(''.join(i))
