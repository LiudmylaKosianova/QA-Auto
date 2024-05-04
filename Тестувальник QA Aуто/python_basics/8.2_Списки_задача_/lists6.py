
# Знаходження макимального елементу масиву
def max_list(mas):
    max = mas[0]

    for i in mas:
        if max < i:
            max = i

    return max

# Обчислення кількості додатніх елементів
def positive_count(mas):
    number = 0
    for i in mas:
        if i > 0:
            number += 1
    
    return number

# обчислення середнього арифметичного значення
def average_temperature(mas):
    s = 0
    for i in mas:
        s = s + i

    return s/len(mas)




temperature = [3, 5, -1, -3, -2, 1, 3]
max_temp = max_list(temperature)
print("Масимальна температура:", max_temp)
positive_temp =  positive_count(temperature)
print("Кількість днів з плюсовою температурою:", positive_temp)
average_temp = average_temperature(temperature)
print("Середня температура:", average_temp)