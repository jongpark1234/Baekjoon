n = int(input())
sequence = [0, 1, 1]
for i in range(3, n + 1):
    sequence.append(sequence[i - 1] + sequence[i - 2])
print(sequence[n])
