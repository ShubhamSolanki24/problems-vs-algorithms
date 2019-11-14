import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_found = float('inf')
    max_found = float('-inf')

    for item in ints:
        if item < min_found:
            min_found = item

        if item > max_found:
            max_found = item

    return min_found, max_found


if __name__ == '__main__':
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
