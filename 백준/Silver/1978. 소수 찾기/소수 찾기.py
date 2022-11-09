import sys
input = sys.stdin.readline

n =int(input())
lst = list(map(int, input().split()))
result = 0

def prime(x):
    cnt = 2
    res = 1
    if x == 1:
        return 0
    else:
        while cnt < x:
            if x % cnt == 0:
                res -= 1
                return res
            else:
                cnt += 1
    return res

for i in range(n):
    result += prime(int(lst[i]))

print(result)