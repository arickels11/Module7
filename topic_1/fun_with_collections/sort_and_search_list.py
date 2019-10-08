"""CIS 189
Alex Rickels
Topic 1 Assignment 3"""


def sort_list(get_list):
    """
    :param get_list: gets list from user
    :return: returns the list sorted from smallest to largest
    """
    get_list.sort()
    return get_list  # returning the list after it is sorted, because it is how i could test it worked in the main :)


def search_list(get_list, index_check):
    """
    :param get_list: get list from user
    :param index_check: get number to check if in list from user
    :return: index of the determined number in the list
    """
    try:
        return get_list.index(index_check)
    except ValueError:
        return -1


if __name__ == '__main__':
    test_list = [1, 3, 5, 7, 7, 6]
    print(search_list(test_list, 5))
    print(sort_list(test_list))
