import time
"""
в быстрой сортировке лучше всего выбирать элемент в центре списка для наибыстрейшей скорости его выполнения О=(n * log n)
"""

nums = [5,4,3,2,1]
start = time.time()


def quicksort(array):
    if len(array) <= 1:
        return array

    else:
        main_elem = array[0]
        less = [i for i in array if i < main_elem]
        greater = [i for i in array if i > main_elem]

    return quicksort(less) + [main_elem] + quicksort(greater)


time.sleep(1)
end = time.time() - start
print(quicksort(nums))
print(end)