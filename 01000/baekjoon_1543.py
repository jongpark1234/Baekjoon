docs = input()
word = input()
index = 0
count = 0
while index <= len(docs) - len(word):
    if docs[index:index + len(word)] == word:
        count += 1
        index += len(word)
    else:
        index += 1
print(count)
