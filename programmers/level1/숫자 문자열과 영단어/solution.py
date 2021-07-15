def solution(s):
    answer = 0
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i,v in enumerate(nums):
        s = s.replace(v,str(i))
    
    answer = int(s)
    
    return answer
