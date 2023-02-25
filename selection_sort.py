list = [3, 4, 1, 6, 2, 5]


def find_smallest(arr):
    smallest_array = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest_array > arr[i]:
            smallest_index = i
            smallest_array = arr[i]
    return smallest_index


def sorting_def(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        """ строкой ниже нужен 'arr.pop', так как при нахождении наименьшего числа много итераций к ряду массив будет заполнен одним наименьшим числом """
        new_array.append(arr.pop(smallest))
    return new_array


print(sorting_def(list))
