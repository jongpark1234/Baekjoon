db = [
    [9.23076, 26.7, 1.835],
    [1.84523, 75, 1.348],
    [56.0211, 1.5, 1.05],
    [4.99087, 42.5, 1.81],
    [0.188807, 210, 1.41],
    [15.9803, 3.8, 1.04],
    [0.11193, 254, 1.88]
]
for _ in range(int(input())):
    result = 0
    score = list(map(int, input().split()))
    for i in range(7):
        if i in [0, 3, 6]:
            result += int(db[i][0] * (db[i][1] - score[i]) ** db[i][2])
        else:
            result += int(db[i][0] * (score[i] - db[i][1]) ** db[i][2])
    print(result)
