my_dict = {
    'tuple': (4, False, 87.5, 'Pen', '5'),
    'list': [455, 'right', True, 'Samsung', 455],
    'dict': {
        'title': "Atomic habits",
        'author': "James Clear",
        'year': 2018,
        'raiting': 4.5,
        'description': "The book is a practical guide to building good habits"},
    'set': {1, 'two', 3, 'four', 5}
}

# выведите на экран последний элемент
print(my_dict["tuple"][-1])
print('')

# добавьте в конец списка еще один элемент
my_dict['list'].append(100)
print(my_dict['list'])
print('')

# удалите второй элемент списка
my_dict['list'].pop(1)
print(my_dict['list'])
print('')

# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'][('I am a tuple',)] = "I am a value of tuple"
print(my_dict['dict'])
print('')

# удалите какой-нибудь элемент
del my_dict['dict']['description']
print(my_dict['dict'])
print('')

# добавьте новый элемент в множество
my_dict['set'].add('six')
print(my_dict['set'])
print('')

# удалите элемент из множества
my_dict['set'].remove(5)
print(my_dict['set'])
print('')

# В конце выведите на экран весь словарь
print(my_dict)
