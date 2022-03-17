for _ in range(int(input())):
    name, grade = input().split()
    grade = int(grade)
    if grade >= 97:
        rank = 'A+'
    elif grade >= 90:
        rank = 'A'
    elif grade >= 87:
        rank = 'B+'
    elif grade >= 80:
        rank = 'B'
    elif grade >= 77:
        rank = 'C+'
    elif grade >= 70:
        rank = 'C'
    elif grade >= 67:
        rank = 'D+'
    elif grade >= 60:
        rank = 'D'
    else:
        rank = 'F'
    print(name, rank)
