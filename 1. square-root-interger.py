# def sqrt(number):
#     return int(number ** (1 / 2))

def sqrt(number):  # O(logn)
    if number < 0:
        print(number, ' is invalid, must be greater than or equal to 0')
        return -1
    result = 0
    while (result + 1) ** 2 <= number:
        result += 1
    return result


if __name__ == '__main__':
    print("Pass" if (-1 == sqrt(-120)) else "Fail")
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print("Pass" if (31 == sqrt(999)) else "Fail")
    print("Pass" if (92 == sqrt(8572)) else "Fail")
    print("Pass" if (436 == sqrt(190292)) else "Fail")
