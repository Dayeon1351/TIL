input = 20


def fibo_recursion(n):
    if n < 3:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765