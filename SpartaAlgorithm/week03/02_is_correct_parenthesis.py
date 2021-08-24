s = "(())()"


def is_correct_parenthesis(string):
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return True if not stack else False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))