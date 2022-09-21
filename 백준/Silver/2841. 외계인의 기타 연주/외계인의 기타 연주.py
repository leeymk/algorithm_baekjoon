import sys

N, p = map(int, sys.stdin.readline().split())
line = [[0] for _ in range(N+1)]
cnt = 0

for i in range(N):
    line_num, flat_num = map(int, sys.stdin.readline().split())

    while line[line_num][-1] > flat_num:
        line[line_num].pop()
        cnt += 1

    if line[line_num][-1] == flat_num:
        continue

    line[line_num].append(flat_num)
    cnt += 1

print(cnt)