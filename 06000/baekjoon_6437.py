idx = 0
while True:
    idx += 1
    p, s = map(int, input().split())
    if p == s == 0:
        break
    temp = p - s
    print(f"Hole #{idx}\n{'Birdie' if temp == 1 else 'Bogey' if temp == -1 else 'Hole-in-one' if temp == 2 and s == 1 else 'Eagle' if temp == 2 else 'Double eagle' if temp == 3 else 'Par' if temp == 0 else 'Double Bogey'}.\n")
