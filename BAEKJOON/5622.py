numbers = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
s = input()
result = 0
for i in range(len(s)):
    for number in numbers:
        if s[i] in number:
            result += numbers.index(number) + 3
            break
print(result)