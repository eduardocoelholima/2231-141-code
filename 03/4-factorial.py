def f(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        fact_rest = f(n - 1)
        return n * fact_rest


print(f(4))
# print(factorial(10))
# print(factorial(100))
# print(factorial(2000))
