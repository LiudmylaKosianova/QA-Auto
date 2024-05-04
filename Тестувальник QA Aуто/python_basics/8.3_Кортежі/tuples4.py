gas_volume = (153, 220, 0)
value_to_remove = 220
idx = gas_volume.index(value_to_remove)
print("Значення, які знаходяться до того, яке ми видаляємо", gas_volume[:idx])
print("Значення, які знаходяться після того, яке ми видаляємо", gas_volume[idx+1:])
new_gas_volume = gas_volume[:idx] + gas_volume[idx+1:]
print("Новий кортеж", new_gas_volume)
