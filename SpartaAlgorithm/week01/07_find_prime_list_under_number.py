input = 20


def find_prime_list_under_number(number):
    nums = [i for i in range(2,number+1)]

    for i in range(2,int(number**1/2)+1):
        for j in range(i*2,number+1,i):
            if j in nums:
                nums.remove(j)

    return nums

result = find_prime_list_under_number(input)
print(result)