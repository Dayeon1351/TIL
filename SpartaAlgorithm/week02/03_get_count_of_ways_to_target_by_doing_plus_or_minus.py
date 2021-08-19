numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array,target,value,index):
    result = 0
    if index == len(array): 
        return 1 if target == value else 0
    else:
        num = array[index]
        result+= get_count_of_ways_to_target_by_doing_plus_or_minus(array,target,value+num,index+1)
        result+= get_count_of_ways_to_target_by_doing_plus_or_minus(array,target,value-num,index+1)
    
    return result

        

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers,target_number,0,0))  # 5를 반환해야 합니다!