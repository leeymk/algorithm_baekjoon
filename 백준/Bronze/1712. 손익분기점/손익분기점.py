import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
cnt = 0

if c <= b:
    print(-1)

else:
    print(a//(c-b)+1)
