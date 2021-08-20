import string
from collections import deque
def solution(s, n):
    answer = ''
    lower = deque(list(string.ascii_lowercase))
    upper = deque(list(string.ascii_uppercase))
    
    for i in s:
        if i >= 'a' and i <='z':
            idx = lower.index(i)
            lower.rotate(-n)
            c = lower[idx]
        elif i >='A' and i <='Z':
            idx = upper.index(i)
            upper.rotate(-n)
            c = upper[idx]
            
        answer += c if i != " " else " "
            
    return answer
