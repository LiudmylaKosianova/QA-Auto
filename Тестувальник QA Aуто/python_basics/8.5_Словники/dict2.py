user = {
    'name': 'Sergii',
    'age': 100500,
    'profession': 'Golf Player',
    'country': 'Ukraine'
}
print(user)

print(user['age'])

print(user['profession'])
user['profession'] = 'Automation QA'
print(user['profession'])

key = 'country'
print(user[key])
user[key] = 'Ukraine, Poland'
print(user[key])
print(user.get(key))
