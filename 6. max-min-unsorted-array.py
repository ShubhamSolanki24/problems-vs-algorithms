import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        print('Invalid Length of ints')
        return float('inf'), float('-inf')

    min_found = ints[0]
    max_found = ints[0]

    for item in ints[1:]:
        if item < min_found:
            min_found = item

        if item > max_found:
            max_found = item

    return min_found, max_found


if __name__ == '__main__':
    test1 = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(test1)
    print("Pass" if ((0, 9) == get_min_max(test1)) else "Fail")

    test2 = [i for i in range(0, 100)]  # a list containing 0 - 9
    random.shuffle(test2)
    print("Pass" if ((0, 99) == get_min_max(test2)) else "Fail")

    test3 = [i for i in range(0, 1000)]  # a list containing 0 - 9
    random.shuffle(test3)
    print("Pass" if ((0, 999) == get_min_max(test3)) else "Fail")
