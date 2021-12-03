import heapq
import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
heapq.heapify(nums)

ans = 0
while len(nums) > 1:
    temp = heapq.heappop(nums) + heapq.heappop(nums)
    ans += temp
    heapq.heappush(nums,temp)

print(ans)
