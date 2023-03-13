nums = [1, 2, 3, 4, 5]
total = 0


def recursion_len(array):
    global total
    if len(array) == 0:
        return total
    else:
        total += 1
        return recursion_len(array[1:])


print(recursion_len(nums))