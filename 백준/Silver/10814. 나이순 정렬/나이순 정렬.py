import sys
input = sys.stdin.readline

N = int(input())
res = []
for _ in range(N):
    res.append(list(input().split()))
res.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(res[i][0], res[i][1])