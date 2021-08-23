from collections import deque

def find_correct(string):
    stack = []
    for c in string:
        if c == "[" or c == "{" or c == "(":
            stack.append(c)
        else:
            if "[" in stack and c == "]" and stack[-1] == "[":
                stack.pop()
            elif "{" in stack and c == "}" and stack[-1] == "{":
                stack.pop()
            elif "(" in stack and c == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return 0
    
    return 1 if not stack else 0
                
                
def solution(s):
    answer = 0
    deq = deque(list(s))
    
    for i in range(len(s)):
        deq.rotate(-1)
        string = "".join(deq)
        answer += find_correct(string)
        
    return answer
