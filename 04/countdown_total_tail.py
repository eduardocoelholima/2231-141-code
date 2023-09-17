def count_down_total_tail(n, total):
  if n < 0: # base case
    return total
  else:     # recursive case
    # complete a unit of work
    print(n)
    # prepare
    next = n - 1
    total += n
    # make the recursive call
    return count_down_total_tail(next, total)

print(count_down_total_tail(6,0))