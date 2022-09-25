import sys
input = sys.stdin.readline

def d(n):
    return n + n%10 + (n%100)//10 + (n%1000)//100 + (n%10000)//1000 + n//10000

A = set()

for i in range(1, 10001):
    A.add(i)

for i in range(1, 10001):
    if d(i) in A:
        A.remove(d(i))

A = list(A)

for a in A:
    print(a)