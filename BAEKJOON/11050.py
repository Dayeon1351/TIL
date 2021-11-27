# n!/(k!(n-k)!) 0<=k<=n
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

n,k = map(int,input().split())
ans = factorial(n)//(factorial(k)*factorial(n-k))
print(ans)