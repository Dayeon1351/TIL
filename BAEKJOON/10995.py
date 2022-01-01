n = int(input())
star = "* " * n
for i in range(1,n+1):
    print(" " + star if i % 2 == 0 else star) 