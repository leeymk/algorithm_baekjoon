N, K = map(int, input().split())

data = list(True for _ in range(N+1))
tmp = 0

for i in range(2,N+1):
    for j in range(i,N+1,i):
        if data[j] != False:
            data[j] = False
            tmp += 1
            if tmp == K:
                print(j)

    