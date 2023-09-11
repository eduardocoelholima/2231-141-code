from time import perf_counter

N = 30
PROGRESS = ['\\', '|', '/']
PROGRESS_COUNT = 0


def update_progress():
    global PROGRESS_COUNT
    PROGRESS_COUNT = (PROGRESS_COUNT + 1) % 3
    print('\b' + PROGRESS[PROGRESS_COUNT], end='')


def fibonacci_normal(n):
    if n < 2:
        return n
    else:
        update_progress()
        return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)


def fibonacci_memory(n, memory={}):
    if n < 2:
        return n
    else:
        update_progress()
        if n not in memory:
            memory[n] = fibonacci_memory(n - 1, memory) + fibonacci_memory(n - 2, memory)
        return memory[n]


def main():
    print('Staring speed comparison')
    start = perf_counter()
    print('Running fibonacci_normal(' + str(N) + ')')
    fibonacci_normal(N)
    print()
    print(f'{round(perf_counter() - start, 3)} seconds')
    start = perf_counter()
    print('Running fibonacci_memory(' + str(N) + ')')
    fibonacci_memory(N)
    print()
    print(f'{round(perf_counter() - start, 3)} seconds')
    print('Speed comparison complete')


if __name__ == '__main__':
    main()
