seat_count = 9
vip_seat_array = [4, 7]

memo_fibo = {
    1 : 1,
    2 : 2,
    3 : 3
}
def fibo(n,memo_fibo):
    if n in memo_fibo:
        return memo_fibo[n]
    else:
        memo_fibo[n] = fibo(n-1,memo_fibo) + fibo(n-2,memo_fibo)
        return memo_fibo[n]



def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    total = 1
    current_index = 0
    for fixed in fixed_seat_array:
        fixed_index = fixed - 1
        result = fibo(fixed_index - current_index,memo_fibo)
        total *= result
        current_index = fixed_index + 1
    
    result = fibo(total_count - current_index,memo_fibo)
    total *= result
    
    return total


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))