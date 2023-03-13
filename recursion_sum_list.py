nums = [1,2,3,4,5,6,7,8,9,10]


def recursion_sum(array):
    if len(array) == 0:
        return 0
    return array[0] + recursion_sum(array[1:])


print(recursion_sum(nums))
