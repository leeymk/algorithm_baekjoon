import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    word = str(input())
    lst = [-1]
    word_set = set(word)
    for i in range(len(word)):
        if word[i] == lst[-1]:
            continue
        else:
            lst.append(word[i])
    if len(lst)-1 == len(word_set):
        cnt += 1

print(cnt)
