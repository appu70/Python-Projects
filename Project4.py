""" BST
----------------------------------------
"""
import random

foods = [
    'Aloo Gobi',
    'Butter Chicken',
    'Fish curry',
    'Palak paneer',
    'Spinach curry with fresh cheese',
    'Doughy',
    'Crisp papadum',
    'Chana masala',
    'Chickpea stew'
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(foods) # randomly choose a food

print('What to eat Today?')
print(selected)