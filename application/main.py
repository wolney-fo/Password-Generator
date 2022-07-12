from random import randint
import clipboard as c
from win10toast import ToastNotifier


# Create password
def generate_password(len=22):
    characters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[]^_`{}~'''
    password = ''

    for i in range(len):
        password += characters[randint(0, 91)]
    
    return password

# Copy to clipboard
c.copy(generate_password())


# Send notification
toast = ToastNotifier()

toast.show_toast(
    "Password Generator",
    "Password created and copied to clipboard. Use 'Ctrl + V' or '⌘ + V' to paste anywhere 🔐.",
    duration = 10,
    icon_path = "../icons/icon.ico",
    threaded = True,
)
