import sys
t = int(sys.stdin.readline())
for i in range(t):
    temp = 0
    count = 0
    string = sys.stdin.readline().rstrip()
    middle = int(len(list(string)) / 2)
    fs, ss = list(string[:middle]), list(string[middle:])
    ss.reverse()
    if (len(fs) != (len(ss))): # When String length is odd
        if (fs == ss[:-1]): # same
            pass
        else:
            for j in range(len(fs)):
                if count == 2:
                    break
                elif (fs[j] == ss[j + temp]):
                    pass
                else:
                    temp += 1
                    j -= 1
                    count += 1
    else: # When String length is even
        if (fs == ss): # same
            pass
        else:
            for j in range(len(fs)):
                if count == 2:
                    break
                elif (fs[j] == ss[j]):
                    pass
                else:
                    count += 1
    print(count)
