
words = input().upper()
words_uni = list(set(words))
lst = []
for word in words_uni:
    cnt = words.count(word)
    lst.append(cnt)

if lst.count(max(lst)) > 1:
    print('?')
else:
    max_index = lst.index(max(lst))
    print(words_uni[max_index])