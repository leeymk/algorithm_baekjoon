n = int(input())
num = n
cnt = 2
while num >= (cnt//2):
    if num % cnt == 0:
        print(cnt)
        num = num // cnt
        cnt = 2
    else:
        cnt += 1