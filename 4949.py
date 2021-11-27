import sys

def check_correct(line):
    stack = []
    for s in line:
        if s == "(" or s == "[":
            stack.append(s)
        elif not stack and (s == ")" or s == "]"):
            break
        elif stack:
            if s == ")" and stack[-1] == "(":
                stack.pop()
            elif s == "]" and stack[-1] == "[":
                stack.pop()
            elif (s == ")" and stack[-1] != "(") or (s == "]" and stack[-1] != "["):
                break
        
    else:
        if not stack:
            return True
        
    return False


for line in sys.stdin:
    if line == ".\n":
        break

    if check_correct(line):
        print("yes")
    else:
        print("no")

