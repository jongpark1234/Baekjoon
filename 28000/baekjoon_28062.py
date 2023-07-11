n = int(input())
a = list(map(int, input().split()))
oddA, evenA = [i for i in a if i & 1], [i for i in a if ~i & 1]
print(sum(oddA) + sum(evenA) - (min(oddA) if len(oddA) & 1 else 0))
