"""CIS 189
Alex Rickels
Topic 4 Assignment 1"""
import array as arr


def search_array(get_array, index_check):
    """
    :param get_array: array to check
    :param index_check: number to check if in array
    :return: index number
    """
    try:
        return get_array.index(index_check)
    except ValueError:
        return -1


def sort_array(unsorted_array):
    reg_list = unsorted_array.tolist()
    reg_list.sort()
    sorted_array = ('d', reg_list)
    return sorted_array  # using a return to return the new array after it was sorted


if __name__ == '__main__':
    zarray = arr.array('d', [3.4, 8.7, 7.7, 9.6])
    print(search_array(zarray, 8.7))
    print(sort_array(zarray))
