user = {
    'name': 'Sergii',
    'age': 100500,
    'profession': 'Golf Player',
    'country': 'Ukraine'
}
key_list = user.keys()
print(key_list)
print('age' in key_list)

del user['age']
print(key_list)
print('age' in key_list)

