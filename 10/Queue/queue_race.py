from cs_queue import *
import time

SIZE = 500000

list_queue = list()
start = time.perf_counter()
for i in range(SIZE):
    list_queue.append(i)
while len(list_queue) > 0:
    list_queue.pop(0)
stop = time.perf_counter()
elapsed_time = stop - start
print('List Queue time for ', SIZE, ' = ', elapsed_time)


node_queue = make_empty_queue()
start = time.perf_counter()
for i in range(SIZE):
    enqueue(node_queue, i)
while not is_empty(node_queue) > 0:
    dequeue(node_queue)
stop = time.perf_counter()
elapsed_time = stop - start
print('Node Queue time for ', SIZE, ' = ', elapsed_time)