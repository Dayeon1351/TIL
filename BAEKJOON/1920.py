import sys
n = int(sys.stdin.readline())
arr = set(sys.stdin.readline().split())

m = int(sys.stdin.readline())
num = sys.stdin.readline().split()

for i in num:
    flag = 1 if i in arr else 0
    print(flag)
