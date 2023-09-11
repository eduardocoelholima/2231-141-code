def print_nums_rec(finish, current):
    if current == finish:
        print(current)
        return current
    else:
        print(current)
        next_val = current + 1
        total = current + print_nums_rec(finish, next_val)
        return total

x = print_nums_rec(6, 1)

print(x)

