import re
def solution(files):
    answer = []
    for file in files:
        # '+' : 1회 이상의 일치와 반복
        # '*' : 0회 이상의 일치와 반복
        # '.' : 개행문자를 포함한 모든 문자
        head,num,tail = re.match('([^0-9]+)([0-9]+)(.*)',file).groups()     # tail은 빈문자열 일 수도 있다.
        answer.append([head,num,tail])
    answer.sort(key = lambda x : (x[0].lower(),int(x[1])))
    
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    
    return answer
  

import re
# 정렬의 기준이 되는 key 반환
def key(file):
    head,num,tail = re.match('([^0-9]+)([0-9]+)(.*)',file).groups()
    return [head.lower(),int(num)]
    
def solution(files):
    answer = []
    answer = sorted(files,key = lambda x : key(x))
    return answer
 

