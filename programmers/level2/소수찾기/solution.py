from itertools import permutations

def solution(numbers):
    answer = 0
    nums = []
    for i in range(1,len(numbers)+1):
        for n in permutations(list(numbers),i):
            num = int("".join(n))
            if num != 0 and num != 1 and num not in nums:
                nums.append(num)

                
    for n in nums:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                break
        else:
            answer+=1
            
    return answer
