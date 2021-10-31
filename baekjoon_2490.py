rank = ['D', 'C', 'B', 'A', 'E']
for i in range(3):
    print(rank[sum(list(map(int, input().split())))])
