for _ in range(int(input())):
    cm, kg = map(int, input().split())
    bmi = kg / (cm / 100) ** 2
    if cm < 140.1:
        result = 6
    elif cm < 146:
        result = 5
    elif cm < 159:
        result = 4
    elif cm < 161:
        if 16 <= bmi < 35:
            result = 3
        elif bmi < 16 or 35 <= bmi:
            result = 4
    elif cm < 204:
        if 20 <= bmi < 25:
            result = 1
        elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
            result = 2
        elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
            result = 3
        else:
            result = 4
    else:
        result = 4
    print(result)
