string = list(map(str, input().upper()))
string_set = list(set(string))
count_list = []
for i in string_set:   
    count = string.count(i)
    count_list.append(count)
if count_list.count(max(count_list)) > 1:   print("?")
else:   print(string_set[count_list.index(max(count_list))])