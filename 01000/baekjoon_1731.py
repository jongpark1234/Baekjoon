seq = [int(input()) for _ in range(int(input()))]
if seq[2] - seq[1] == seq[1] - seq[0]:
    print(seq[-1] + seq[1] - seq[0])
else:
    print(seq[-1] * seq[1] // seq[0])
