import itertools
def strsum(arr):
    result = ''.join(arr)
    return result
n = int(input())
k = int(input())
stack = []
for i in range(n):
    stack.append(input())
result = list(set(map(strsum, itertools.permutations(stack, k))))
print(result, type(result))
print(len(result))