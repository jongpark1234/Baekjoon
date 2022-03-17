n = int(input())
cost = 0
SA = 0
ZI = 0
ZA = 0
for i in range(n):
    place = input()
    if place == 'botswana':
        pass
    elif place == "ethiopia":
        cost += 50
    elif place == "kenya":
        cost += 50
    elif place == "namibia":
        if SA:
            cost += 40
        else:
            cost += 140
    elif place == "south-africa":
        SA = 1
    elif place == "tanzania":
        cost += 50
    elif place == "zambia":
        ZA = 1
        if ZI:
            cost += 20
        else:
            cost += 50
    elif place == "zimbabwe":
        ZI = 1
        if ZA:
            pass
        else:
            cost += 30
    if place != "zambia" and place != "zimbabwe":
        ZA = 0
        ZI = 0
print(cost)
