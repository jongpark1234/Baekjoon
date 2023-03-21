n = int(input())
votelist = list(map(int, input().split()))
print('INVALID' if votelist.count(0) >= n / 2 else 'APPROVED' if sum(votelist) > 0 else 'REJECTED')
