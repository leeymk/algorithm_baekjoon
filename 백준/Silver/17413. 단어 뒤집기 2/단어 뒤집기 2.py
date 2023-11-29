import sys

S = sys.stdin.readline().strip()+' '
# S = input().strip()+' '
stack = []
cnt = 0
result = ''
for i in S:
    if i == '<':
        cnt = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == '>':
        cnt = 0
        for _ in range(len(stack)):
            result += stack.pop(0)
            
    if i == ' ' and cnt == 0:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
    
print(result)