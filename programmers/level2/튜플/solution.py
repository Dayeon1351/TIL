import re
import collections
def solution(s):
    answer = []
    
    n = re.sub('[^0-9|,]',"",s)
    nums = n.split(',')
    
    cnt = collections.Counter(nums)
    answer = [0]*len(cnt)
    
    for v,i in cnt.items():
        answer[len(cnt)-i] = int(v)
    
    return answer
