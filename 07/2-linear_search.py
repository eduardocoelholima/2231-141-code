from typing import Any


def find_in_list(element:Any, search_list:list) -> bool:
    result = False
    for item in search_list:
        if item == element:
            result = True
            # print(item)
            break
    return result

def main():
    da_list = ['a', 1, False, 1.3, [1,2,3]]
    print(find_in_list('a', da_list))
    print(find_in_list(2, da_list))
    print(find_in_list([1,2], da_list))

    print(find_in_list(True, da_list))  # Tricky!!

main()