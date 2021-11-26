nums = list(input().split())
ans = sum([int(n)**2 for n in nums]) % 10
print(ans)


