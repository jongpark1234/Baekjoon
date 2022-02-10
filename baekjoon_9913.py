Dict = {}
for i in [int(input()) for _ in range(int(input()))]:
    try:
        Dict[i] += 1
    except:
        Dict[i] = 1
print(max(Dict.values()))
