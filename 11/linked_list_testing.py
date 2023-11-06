import linked_list_immutable
import linked_list_mutable


SIZE = 3


def main():
    print("*****  Testing Immutable List  *****")
    print('Create Empty List')
    immutable_linked_list = linked_list_immutable.make_empty_list()
    original_list = immutable_linked_list
    print(linked_list_immutable.to_str(original_list), linked_list_immutable.to_str(immutable_linked_list))
    print('Append Some Values')
    for i in range(1, SIZE + 1):
        immutable_linked_list = linked_list_immutable.append(immutable_linked_list, i)
    print(linked_list_immutable.to_str(original_list), linked_list_immutable.to_str(immutable_linked_list))
    print('Get A Value')
    print(linked_list_immutable.get_value(immutable_linked_list, SIZE // 2))
    print('Set A Value')
    immutable_linked_list = linked_list_immutable.set_value(immutable_linked_list, 7, SIZE // 2)
    print(linked_list_immutable.to_str(original_list), linked_list_immutable.to_str(immutable_linked_list))
    print('Check For A Value')
    print(SIZE, linked_list_immutable.contains(immutable_linked_list, SIZE))
    print(SIZE + 1, linked_list_immutable.contains(immutable_linked_list, SIZE + 1))
    print('Index Of A Value')
    print(SIZE, linked_list_immutable.index_of(immutable_linked_list, SIZE))
    print(SIZE + 1, linked_list_immutable.index_of(immutable_linked_list, SIZE + 1))
    print('Remove A Value')
    immutable_linked_list = linked_list_immutable.remove_value(immutable_linked_list, 7)
    print(linked_list_immutable.to_str(original_list), linked_list_immutable.to_str(immutable_linked_list))
    print('Insert A Value')
    immutable_linked_list = linked_list_immutable.insert_before_index(immutable_linked_list, 'New', SIZE // 2)
    print(linked_list_immutable.to_str(original_list), linked_list_immutable.to_str(immutable_linked_list))
    print('Concatenate A List')
    immutable_linked_list2 = linked_list_immutable.make_empty_list()
    for i in range(SIZE + 10, SIZE + 14):
        immutable_linked_list2 = linked_list_immutable.append(immutable_linked_list2, i)
    immutable_linked_list = linked_list_immutable.concatenate(immutable_linked_list, immutable_linked_list2)
    print(linked_list_immutable.to_str(immutable_linked_list), linked_list_immutable.to_str(immutable_linked_list2))
    print("*****  Done Testing Immutable List  *****")
    print()

    print("*****  Testing Mutable List  *****")
    print('Create Empty List')
    mutable_linked_list = linked_list_mutable.make_empty_list()
    print(linked_list_mutable.to_str(mutable_linked_list))
    print('Append Some Values')
    for i in range(1, SIZE + 1):
        linked_list_mutable.append(mutable_linked_list, i)
    print(linked_list_mutable.to_str(mutable_linked_list))
    print('Get A Value')
    print(linked_list_mutable.get_value(mutable_linked_list, SIZE // 2))
    print('Set A Value')
    linked_list_mutable.set_value(mutable_linked_list, 7, SIZE // 2)
    print(linked_list_mutable.to_str(mutable_linked_list))
    print('Check For A Value')
    print(SIZE, linked_list_mutable.contains(mutable_linked_list, SIZE))
    print(SIZE + 1, linked_list_mutable.contains(mutable_linked_list, SIZE + 1))
    print('Index Of A Value')
    print(SIZE, linked_list_mutable.index_of(mutable_linked_list, SIZE))
    print(SIZE + 1, linked_list_mutable.index_of(mutable_linked_list, SIZE + 1))
    print('Remove A Value')
    linked_list_mutable.remove_value(mutable_linked_list, 7)
    print(linked_list_mutable.to_str(mutable_linked_list))
    print('Insert A Value')
    linked_list_mutable.insert_before_index(mutable_linked_list, 'New', SIZE // 2)
    print(linked_list_mutable.to_str(mutable_linked_list))
    print('Concatenate A List')
    mutable_linked_list2 = linked_list_mutable.make_empty_list()
    for i in range(SIZE + 10, SIZE + 14):
        linked_list_mutable.append(mutable_linked_list2, i)
    linked_list_mutable.concatenate(mutable_linked_list, mutable_linked_list2)
    print(linked_list_mutable.to_str(mutable_linked_list), linked_list_mutable.to_str(mutable_linked_list2))
    print("*****  Done Testing Mutable List  *****")

if __name__ == '__main__':
    main()