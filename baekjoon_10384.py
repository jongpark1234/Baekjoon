import sys
n = int(sys.stdin.readline())
for i in range(n):
    adict = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
    s = sys.stdin.readline().rstrip().lower()
    s = ''.join(filter(str.isalpha, s))
    for j in range(len(s)):
        adict[s[j]] += 1
    pangram = min(list(adict.values()))
    if pangram >= 3:
        print(f'Case {i + 1}: Triple pangram!!!')
    elif pangram == 2:
        print(f'Case {i + 1}: Double pangram!!')
    elif pangram == 1:
        print(f'Case {i + 1}: Pangram!')
    else:
        print(f'Case {i + 1}: Not a pangram')
