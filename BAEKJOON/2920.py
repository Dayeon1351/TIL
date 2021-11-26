nums = list(map(int,input().split()))

result = ""
total = 0
for i in range(len(nums)-1):
    n = nums[i+1] - nums[i]
    if abs(n) != 1:
        result = "mixed"
        break
    total += n
else:
    result = "ascending" if total > 0 else "descending"

print(result)
