from collections import Counter
numlist = [int(input()) for i in range(10)]
print(sum(numlist) // 10, Counter(numlist).most_common()[0][0], sep='\n')
