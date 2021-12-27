n = int(input())
arr = list(map(int,input().split()))
dp_in = [0] * n
dp_de = [0] * n
dp_bitonic = [0] * n

for i in range(n):
    for j in range(n):
        if arr[i] > arr[j] and dp_in[i] < dp_in[j]:
            dp_in[i] = dp_in[j]
    dp_in[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[i] > arr[j] and dp_de[i] < dp_de[j]:
            dp_de[i] = dp_de[j]
    dp_de[i] += 1

for i in range(n):
    dp_bitonic[i] = dp_in[i] + dp_de[i] - 1

print(max(dp_bitonic))

