from itertools import combinations
def solution(nums):
    answer = 0

    n = [sum(num) for num in combinations(nums,3)]
    for i in n:
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            answer+=1
            
    return answer
