user = {"name": "Sergii", "age": 100500}

years_old = user.get("years_old")
if years_old is None:
    print("Ключ years_old відсутній")
else:
    print(years_old)

if "years_old" in user:
    print(years_old)
else:
    print("Ключ years_old відсутній")
