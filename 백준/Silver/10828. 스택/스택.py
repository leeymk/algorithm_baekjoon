import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    order = command[0]
    if order == 'push':
        stack.append(command[1])
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])

