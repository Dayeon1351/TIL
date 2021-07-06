def solution(s):
    answer = -1
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    
    answer = 1 if len(stack) == 0 else 0 

    return answer
