def countdown(n):
    total = 0
    while True:
        if n < 0:
            break
        else:
            print(n)
            total = total + n
            n = n - 1
    return total

def countdown(n):
    total = 0
    while n >= 0:
        print(n)
        total = total + n
        n = n - 1
    return total

print(countdown(6))