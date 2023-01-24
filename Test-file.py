import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+'

length = int(input('Input password length: '))

print('\nHere is your password:')
password = ''

for pwd in range(length):
    password += random.choice(chars)

print(password)