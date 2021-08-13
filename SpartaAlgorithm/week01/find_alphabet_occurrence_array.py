from collections import Counter

input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    str = Counter(string.replace(" ","")).most_common()[0][0]
    return str


result = find_max_occurred_alphabet(input)
print(result)
