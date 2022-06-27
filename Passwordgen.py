import random

print('Welcome to your Password Generator.')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate:')
number = int(number)

length = input('Input your Password length: ')
length = int(length)

print('\nhere are your password:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)