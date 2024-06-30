import string
import random


def pass_generator():

    num_letters = random.randint(2, 5)

    num_numbers = random.randint(2, 3)

    num_symbols = random.randint(2, 3)

    alphabet_all = list(string.ascii_letters)
    symbols_all = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    py_password = []

    for i in range(0, num_letters):
        random_letter = random.choice(alphabet_all)
        py_password += [random_letter]

    for i in range(0, num_numbers):
        random_number = str(random.randint(0, 9))
        py_password += [random_number]

    for i in range(0, num_symbols):
        random_symbol = random.choice(symbols_all)
        py_password += [random_symbol]

    random.shuffle(py_password)

    password = ""

    for i in py_password:
        password += i

    return password
