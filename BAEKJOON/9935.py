string = input()
flag = input()
stack = []
len_flag = len(flag)
list_flag = list(flag)

for s in string:
    stack.append(s)
    if stack[-len_flag:] == list_flag:
        del stack[-len_flag:]

print("".join(stack) if stack else "FRULA")
