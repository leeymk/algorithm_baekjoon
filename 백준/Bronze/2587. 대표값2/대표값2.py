# import sys
# input = sys.stdin.readline

lst = [int(input()) for _ in range(5)]
lst = sorted(lst)

print(sum(lst)//5)
print(lst[2])


