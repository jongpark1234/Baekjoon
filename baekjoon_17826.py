scores = list(map(int, input().split()))
score = int(input())
grade = scores.index(score) + 1
if 1 <= grade <= 5:
    print('A+')
elif 6 <= grade <= 15:
    print('A0')
elif 16 <= grade <= 30:
    print('B+')
elif 31 <= grade <= 35:
    print('B0')
elif 36 <= grade <= 45:
    print('C+')
elif 46 <= grade <= 48:
    print('C0')
else:
    print('F')
