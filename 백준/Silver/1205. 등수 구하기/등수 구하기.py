import sys
input = sys.stdin.readline

n, new_grade, p = map(int, input().split())
if n == 0:
    print(1)
else:
    lst = list(map(int, input().split()))
    lst.append(new_grade)
    lst = sorted(lst, reverse=True)
    for i in range(len(lst)):
        if lst[-1] == new_grade and n == p:
            print(-1)
            break
        elif lst[i] == new_grade and i < p:
            print(i+1)
            break
        elif lst[i] == new_grade and i >= p:
            print(-1)
            break
