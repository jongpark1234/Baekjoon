n = int(input())
list1 = [input() for _ in range(n)]
list2 = [input() for _ in range(n)]
print(sum(list1[i] == list2[i] for i in range(n)))
