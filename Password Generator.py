import random
import string


def pass_word():
    password = ''
    lower_count = 0
    upper_count = 0
    number_count = 0
    symbol_count = 0

    lower_target = int(input('How many lower case letters do you want, minimum of 2: '))
    upper_target = int(input('How many upper case letters do you want, minimum of 2: '))
    number_target = int(input('How many numbers do you want, minimum of 2: '))
    symbol_target = int(input('How many symbols do you want, minimum of 2: '))

    while lower_count != lower_target:
        password += (random.choice(string.ascii_lowercase))
        lower_count += 1
        continue

    while upper_count != upper_target:
        password += (random.choice(string.ascii_uppercase))
        upper_count += 1
        continue

    while number_count != number_target:
        password += (random.choice(string.digits))
        number_count += 1
        continue

    while symbol_count != symbol_target:
        password += (random.choice(string.punctuation))
        symbol_count += 1
        continue

    secure_password = list(password)
    random.shuffle(secure_password)
    print('Your Secure Password is:')
    print(''.join(secure_password))


pass_word()
