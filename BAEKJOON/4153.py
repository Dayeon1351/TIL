while 1:
    nums = list(map(int,input().split()))
    if not all(nums):
        break

    nums.sort()
    if nums[0]**2 + nums[1]**2 != nums[2]**2:
        print("wrong")
    else:
        print("right")