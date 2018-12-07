# Code by Jakub Reha


def inputNumber(prompt):

    while True:

        try:

            num = float(input(prompt))
            break
        except ValueError:

            pass
    return num
