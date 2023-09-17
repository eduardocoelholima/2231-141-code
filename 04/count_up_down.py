def count_up(n):
  if n < 0: # base case
    return
  else:     # recursive case
    # prepare for recursion
    next = n - 1
    # make the recursive call
    count_up(next)
    # complete a unit of work
    print(n)

def count_down(n):
  if n < 0: # base case
    return
  else:     # recursive case
    # complete a unit of work
    print(n)
    # prepare
    next = n - 1
    # make the recursive call
    count_down(next)


count_up(6)
count_down(6)