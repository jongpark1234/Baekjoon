temp = 0
t = int(input())
precomputation = []
for i in range(80001):
    temp += i if i % 3 == 0 or i % 7 == 0 else 0
    precomputation.append(temp)
for i in map(int, input().split()):
    print(precomputation[i])
