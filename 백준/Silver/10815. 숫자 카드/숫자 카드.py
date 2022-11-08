import sys
input = sys.stdin.readline

n = int(input())
set_n = set(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))

for i in range(len(lst_m)):
    if lst_m[i] in set_n:
        print(1, end=' ')
    else:
        print(0, end=' ')