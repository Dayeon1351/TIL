input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    all_zero = 0
    all_one = 0

    if string[0] == '0':
        all_one += 1
    else:
        all_zero += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                all_one+=1
            else:
                all_zero+=1
    
    return min(all_zero,all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)