def print_nums_rec(finish, current):
    if current == finish:
        print(current)
    else:
        print(current)
        next_val = current + 1
        print_nums_rec(finish, next_val)


print_nums_rec(3, 1)
