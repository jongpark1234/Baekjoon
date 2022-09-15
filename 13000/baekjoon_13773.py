while True:
    year = int(input())
    if year == 0:
        break
    elif year < 1896:
        print(f'{year} No summer games')
    elif year & 3 == 0:
        if year in [i for i in range(1914, 1919)] + [i for i in range(1939, 1946)]:
            print(f'{year} Games cancelled')
        elif year > 2020:
            print(f'{year} No city yet chosen')
        else:
            print(f'{year} Summer Olympics')
    else:
        print(f'{year} No summer games')
