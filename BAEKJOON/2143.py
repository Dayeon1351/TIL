from collections import defaultdict
import sys
input = sys.stdin.readline
 
t = int(input())

n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))


sum_a = [0] * (n+1)
sum_b = [0] * (m+1)
for i in range(1,n+1):
    sum_a[i] = sum_a[i-1] + a[i-1]

for i in range(1,m+1):
    sum_b[i] = sum_b[i-1] + b[i-1]

dict_sum = defaultdict(int)
for i in range(1,n+1):
    for j in range(i):
        key = sum_a[i] - sum_a[j]
        dict_sum[key]  += 1


result = 0
for i in range(1,m+1):
    for j in range(i):
        key = sum_b[i] - sum_b[j]
        result += dict_sum[t-key]
        
print(result)