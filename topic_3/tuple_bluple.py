"""CIS 189
Alex Rickels
Topic 3 Assignment 1"""


def write_to_file(my_tuple):
    """
    :param my_tuple: tuple to append to file
    :return: appended file
    """
    try:
        with open('student_info.txt', 'a') as f:  # open file
            f.writelines(my_tuple)  # append tuple
            f.close()
    except IOError:
        print("this isn't working")


def get_student_info(**kwargs):
    """
    :param kwargs: keyword argument - name of student
    :return: file with student name and test scores
    """
    bluple_list = []
    for key, value in kwargs.items():
        bluple_list.append('\n' + value + '\n')  # append file with name
    while True:
        scores = (input("What score would you like to add? type -1 to end "))
        if scores == '-1':
            break
        else:
            bluple_list.append(scores + '\t')  # append file with scores from user input

    bluple = tuple(bluple_list)
    write_to_file(bluple)


def read_from_file():
    """
    :return: file with student name and scores printed line by line
    """
    try:
        with open('student_info.txt', 'r') as f:  # print all lines of file
            for line in f:
                print(line)
            f.close()
    except IOError:
        print("this isn't working during the read part")


if __name__ == '__main__':
    get_student_info(name="Alex Rickels")
    get_student_info(name="Pillsbury Doughboy")
    get_student_info(name="Pablo Escobar")
    get_student_info(name="Bernie Sanders")
    read_from_file()
