def fib(n):
    if n < 0:
        return None
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    print("fib(3):", fib(3))


if __name__ == '__main__':
    main()
