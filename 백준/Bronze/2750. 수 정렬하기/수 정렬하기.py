import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    n = int(input())
    lst.append(n)
for i in range(N-1):
    for j in range(N-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for k in lst:
    print(k)