user = {
    'name': 'Sergii',
    'age': 100500,
    'profession': 'Golf Player',
    'country': 'Ukraine'
}

print(user)
user['years_old'] = user['age']
del user['age']
print(user)
