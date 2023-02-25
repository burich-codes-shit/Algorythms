num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
num_search = 13


def binary_srch(list, num):
    low = 0
    high = len(num_list) - 1
    middle = (low + high) // 2

    while middle != num_search:
        middle = (low + high) // 2
        if middle == num_search:
            return middle
        elif middle > num_search:
            high = middle
        else:
            low = middle


print(binary_srch(num_list, num_search))
