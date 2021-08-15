input = "abacabade"


def find_not_repeating_character(string):
    idx = []
    for char in set(string):
        if string.count(char) == 1:
            idx.append(string.index(char))
    
    return "_" if not idx else string[min(idx)] 


result = find_not_repeating_character(input)
print(result)