k = list(map(int, input()))
if len(k) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    exit()
dis = k[0] - k[1]
for i in range(len(k) - 1):
    if k[i] - k[i + 1] != dis:
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
        break
else:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
