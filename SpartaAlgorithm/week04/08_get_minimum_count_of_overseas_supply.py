import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 필요한 양 26
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_date_index = 0
    max_heap = []

    while stock <= k:
        while last_date_index < len(dates) and dates[last_date_index] <= stock:
            heapq.heappush(max_heap,-supplies[last_date_index])
            last_date_index +=1
        
        answer += 1
        pop = heapq.heappop(max_heap)
        stock += -pop


    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))