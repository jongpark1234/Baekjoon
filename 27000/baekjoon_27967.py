def createParenthesis(s: list[str], b: str) -> str:
    idx = 0
    for i in g:
        s[i] = '(' if b[idx] == '1' else ')'
        idx += 1
    return ''.join(s)
n = int(input())
s = list(input())
g = [i for i in range(len(s)) if s[i] == 'G']
temp = (1 << len(g)) - 1
length = len(bin(temp)[2:])
for i in range(temp, -1, -1):
    string = createParenthesis(s[:], bin(i)[2:].rjust(length, '0'))
    try:
        exec(string.replace(')', '),'))
        print(string)
        break
    except:
        continue
