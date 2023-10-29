n = int(input())
s = input()
l = sum(i in s for i in 'roygbiv') == 7
u = sum(i in s for i in 'ROYGBIV') == 7
print('YeS' if l and u else 'yes' if l else 'YES' if u else 'NO!')
