from random import randint
import clipboard as c


def generate_password(len=15):
    characters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[]^_`{}~'''
    password = ''

    for i in range(len):
        password += characters[randint(0, 91)]
    
    return password

# Copy to clipboard
c.copy(generate_password())
