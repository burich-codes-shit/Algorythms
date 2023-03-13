nums = [1, 2, 4, 5, 3, 6, 9, 7, 100, 10]
max_digit = 0


def search_max(array):
    global max_digit
    if len(array) == 0:
        return max_digit
    else:
        if max_digit < array[0]:
            max_digit = array[0]
        else:
            pass
        return search_max(array[1:])


print(search_max(nums))

