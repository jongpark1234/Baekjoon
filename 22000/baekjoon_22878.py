def calc(Arr, n):
    ret = 0
    for i in range(n):
        ret += ((i + 1) * 2 - (n + 1)) * Arr[i]
    return ret * 2
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
Arr1 = [p[i] + q[i] for i in range(n)]
Arr2 = [p[i] - q[i] for i in range(n)]
p.sort();q.sort();Arr1.sort();Arr2.sort()
print(calc(p, n) + calc(q, n) - ((calc(Arr1, n) + calc(Arr2, n)) // 2))
