"""CIS 189
Alex Rickels
Topic 1 Assignment 1"""


def make_list():
    the_list = []
    for x in range(0, 3):
        try:
            user_input = (int(get_input()))
        except ValueError:
            print("try again!")
        else:
            the_list.append(user_input)
    return the_list


def get_input():
    pass


if __name__ == '__main__':
    print(make_list())
