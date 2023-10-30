import random

RUNS = 10
COLLECTION_SIZE = 10000

def coupon_collector(n):
    collection = set()
    boxes = 0
    while len(collection) < n:
        r = random.randint(1, n)
        collection.add(r)
        boxes += 1
    return boxes

def main():
    total = 0
    for i in range(RUNS):
        result = coupon_collector(COLLECTION_SIZE)
        print(result)
        total += result
    print('Average for this run: ', total/RUNS)

if __name__ == '__main__':
    main()