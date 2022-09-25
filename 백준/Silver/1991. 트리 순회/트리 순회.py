import sys
input = sys.stdin.readline
n = int(input())
s = [[0]*3 for _ in range(26)]

def preorder(x):
    print(x, end='')
    if s[ord(x)-65][1] != ".":
        preorder(s[ord(x) - 65][1])
    if s[ord(x)-65][2] != ".":
        preorder(s[ord(x) - 65][2])

def inorder(x):
    if s[ord(x)-65][1] != ".":
        inorder(s[ord(x)-65][1])
    print(x, end="")
    if s[ord(x)-65][2] != ".":
        inorder(s[ord(x)-65][2])

def postorder(x):
    if s[ord(x)-65][1] != ".":
        postorder(s[ord(x)-65][1])
    if s[ord(x)-65][2] != ".":
        postorder(s[ord(x)-65][2])
    print(x, end="")

for i in range(n):
    node, left, right = map(str, input().split())
    item = ord(node) - 65
    s[item][0], s[item][1], s[item][2] = node, left, right
    
preorder("A")
print()
inorder("A")
print()
postorder("A")