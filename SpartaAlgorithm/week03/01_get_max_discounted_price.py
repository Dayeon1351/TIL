shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    result = 0
    
    prices.sort(reverse = True)
    coupons.sort(reverse = True)
    
    for idx in range(len(coupons)):
        if prices:
            result += prices.pop(0) * (100 - coupons[idx]) // 100
    
    if prices:
        result += sum(prices)

    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))