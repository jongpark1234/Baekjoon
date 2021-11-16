scores = sorted([[int(input()), i + 1] for i in range(8)], key = lambda x : x[0])[-5:]
seq = []
total = 0
for i in range(5):
    total += scores[i][0]
    seq.append(scores[i][1])
print(total, ' '.join(map(str, sorted(seq))), sep='\n')
