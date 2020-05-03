# Resolve the problem!!
import string
from random import randint

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
   
    password = []
    longPass = randint(8,16)
    for i in range(0, longPass):
        password.append(chr(randint(33,126)))

    # Se asegura de que siempre halla por lo menos un número, un simbolo, una mayúscula y una minúscula
    password[longPass - 1 ] = chr(randint(48,57))
    password[longPass - 2 ] = SYMBOLS[randint(0,len(SYMBOLS)-1)] 
    password[0] = chr(randint(97,122))
    password[1] = chr(randint(65,90))
    
    return ''.join(password)


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
