n = int(input())

arr = [False,False] + [True] * (n-1)
prime = []

for i in range(2,n + 1):
    if arr[i]:
        prime.append(i)
        for j in range(2*i,n + 1,i):
            arr[j] = False


len_prime = len(prime)
sum_val  = [0] * (len_prime + 1)
for i in range(1,len_prime+1):
    sum_val[i] = sum_val[i-1] + prime[i-1]

start,end = 0,0
cnt = 0
while start < len_prime:
    if sum_val[end] - sum_val[start] < n:
        if end < len_prime:
            end += 1
        else:
            start += 1
    else:
        if sum_val[end] - sum_val[start] == n:
            cnt += 1
        start += 1
    
print(cnt)