while True:
    income = int(input())
    if income == 0:
        break
    elif 1000000 >= income:
        print(income)
    elif 5000000 > income > 1000000:
        print(income * 90 // 100)
    else:
        print(income * 80 // 100)
