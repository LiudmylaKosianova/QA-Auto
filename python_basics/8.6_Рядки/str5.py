user = {
    'name': 'Sergii',
    'age': 100500,
    'profession': 'Golf Player',
    'country': 'Ukraine'
}

formatted_string = "Користувач з ім'ям {}, віком {} проживає у країні {}"

print(formatted_string.format(user['name'], user['age'], user['country']))