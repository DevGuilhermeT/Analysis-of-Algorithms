from random import randint


def valid(password, n):
    if n < 8:
        return False
    symbol = False
    uppercase = False
    lowercase = False
    number = False
    for i in range(0, n):
        if not symbol and 33 <= ord(password[i]) <= 42:
            symbol = True
        if not uppercase and 65 <= ord(password[i]) <= 90:
            uppercase = True
        if not lowercase and 97 <= ord(password[i]) <= 122:
            lowercase = True
        if not number and 48 <= ord(password[i]) <= 57:
            number = True
    return symbol and uppercase and lowercase and number


def random_char():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*'
    i = randint(0, len(chars)-1)
    return chars[i]


def random_password():
    password = ""
    while not valid(password, len(password)):
        size = randint(0, 25)
        password = [0] * size
        for i in range(0, size):
            password[i] = random_char()
    print(''.join(password))

random_password()