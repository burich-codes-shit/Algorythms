list_of_nums = [2,3,1,4,6,9,7,8,5,100]


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        main_elem = array[0]
        less = [i for i in array if i < main_elem]
#        idk = [main_elem] * array.count(main_elem)
        greater = [i for i in array if i > main_elem]

    return quicksort(less) + [main_elem] + quicksort(greater)


print(quicksort(list_of_nums))
