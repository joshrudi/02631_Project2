# Code by Jakub Reha
# Used from course documentation


def inputNumber(prompt):

    while True:

        try:

            num = float(input(prompt))
            break
        except ValueError:

            pass
    return num
