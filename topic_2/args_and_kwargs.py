"""CIS 189
Alex Rickels
Topic 1 Assignment 1"""


#  'Result: name = M gpa = 3.2 course = Python with current average 30.0


def average_scores(*args, **kwargs):
    """
    :param args: scores taken from user
    :param kwargs: name, GPA, and course
    :return: statement regarding name, GPA, course, and average score
    """
    avg = sum(args)/len(args)
    print("Result: ")
    for key, value in kwargs.items():
        print(key, " = ", value)
    print("with current average", str(avg))


if __name__ == '__main__':
    average_scores(90, 91, 92, 93, 100, name='Alex Rickels', GPA=4.0, course='Python')
    average_scores(90, 91, 92, 93, 100, 102, name='Harry Potter', GPA=2.0, course='Potions')
    average_scores(75, 91, 92, 93, name='John Deere', GPA=5.0, course='Tractors')
