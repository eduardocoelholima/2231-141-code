import random
from showtree import *

SIZE = 31

def bt_demo(tr):
    print('In Order', bt_to_string_in_order(tr))
    print('Pre Order', bt_to_string_pre_order(tr))
    print('Post Order', bt_to_string_post_order(tr))
    size = bt_size(tr)
    height = bt_height(tr)
    print('Size', size)
    print('Height', height)
    print('Size to Height Ratio', size/height)
    print('Imbalance', bt_imbalance(tr))
    print('Search for root value', bt_search(tr, tr.value))
    print('Search for not present value', bt_search(tr, 99999))
    btDrawEasy(tr)

def main():
    abt = BinaryTree()
    for i in range(1, SIZE + 1):
        bt_add(abt, i)
    bt_demo(abt)

    # abst = BinarySearchTree()
    # for value in [5, 6, 7, 3, 4, 2, 1, 8, 9]:
    #     bst_add_value(abst, value)
    # bt_demo(abst.root)

    # abst = BinarySearchTree()
    # bst_add_value(abst, 479)
    # while abst.size < SIZE:
    #     value = random.randint(1, SIZE * 2)
    #     if not bst_search(abst.root, value):
    #         bst_add_value(abst, value)
    # bt_demo(abst.root)

    # abst = BinarySearchTree()
    # print(bt_height(abst.root),bt_imbalance(abst.root))
    # for value in [5,4,3,2,1]:
    #     bst_add_value(abst, value)
    #     print(bt_height(abst.root),bt_imbalance(abst.root))

if __name__ == '__main__':
    main()

