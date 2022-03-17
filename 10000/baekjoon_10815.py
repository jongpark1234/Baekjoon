from sys import stdin
n = int(stdin.readline())
nlist = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
mlist = list(map(int, stdin.readline().split()))
nlist.sort()
def bs(arr, temp, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == temp:
            return True
        elif arr[mid] > temp:
            end = mid - 1
        else:
            start = mid + 1
    return False
for i in range(m):
    if bs(nlist, mlist[i], 0, n - 1): print(1, end=' ')
    else: print(0, end=' ')
