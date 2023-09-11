def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    if a == 0:
        return b
    else:
        return gcd(b, a % b)


def main():
    print("gcd(96, 14):", gcd(96, 14))
    print("gcd(14, 96):", gcd(14, 96))
    print("gcd(11,5):", gcd(11, 5))


if __name__ == '__main__':
    main()
