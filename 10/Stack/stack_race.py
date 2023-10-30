from cs_stack import *
import time

SIZE = 5000000

list_stack = list()
start = time.perf_counter()
for i in range(SIZE):
    # list_stack.insert(0, i)
    list_stack.append(i)
while len(list_stack) > 0:
    # list_stack.pop(0)
    list_stack.pop()
stop = time.perf_counter()
elapsed_time = stop - start
print('List Stack time for ', SIZE, ' = ', elapsed_time)


node_stack = make_empty_stack()
start = time.perf_counter()
for i in range(SIZE):
    push(node_stack, i)
while not is_empty(node_stack) > 0:
    pop(node_stack)
stop = time.perf_counter()
elapsed_time = stop - start
print('Node Stack time for ', SIZE, ' = ', elapsed_time)