def fibo(n,result):
    if n in result.keys():
        return result[n]
    else:
        result[n] = list(map(sum,zip(fibo(n-1,result),fibo(n-2,result))))
        return result[n]

m = int(input())
result = {0:[1,0],1:[0,1]}

for i in range(m):
    ans = fibo(int(input()),result)
    print(ans[0],ans[1])

