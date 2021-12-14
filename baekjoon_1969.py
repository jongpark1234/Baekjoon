from sys import stdin, maxsize
n, m = map(int, stdin.readline().split())
dna = [stdin.readline().rstrip() for _ in range(n)]
nucleotide = ['A', 'T', 'G', 'C']
hamming = ''
hamming_distance = 0
for i in range(m):
    temporary = []
    for j in nucleotide:
        distance = 0
        for k in dna:
            if k[i] == j:
                distance += 1
        temporary.append((j, distance))
    temporary.sort(key=lambda x: (-x[1], x[0]))
    hamming += temporary[0][0]
    hamming_distance += n - temporary[0][1]
print(hamming)
print(hamming_distance)
