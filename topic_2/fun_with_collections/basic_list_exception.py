"""CIS 189
Alex Rickels
Topic 1 Assignment 2"""


def make_list():
    """
    :return: list of 3 user inputs
    """
    the_list = []
    for x in range(0, 3):
        try:
            user_input = (int(get_input()))
        except ValueError:
            raise ValueError
        else:
            the_list.append(user_input)
    return the_list


def get_input():
    """
    :return: integer input from user
    """
    return int(input("pick a number "))


if __name__ == '__main__':
    print(make_list())
