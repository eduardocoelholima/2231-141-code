def power(x, y):
    if y < 0:
        return None
    elif y == 0:
        return 1
    else:
        rest = power(x, y-1)
        return x * rest

print(power(2, 4))
print(power(4, 2))
print(power(9, 3))