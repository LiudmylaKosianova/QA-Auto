
wheels_count = int(input("Введіть кількість коліс "))
sits = int(input("Введіть кількість місць "))
guns_count = int(input("Введіть кількість зброї "))


class Banderomobil:
    # your code goes here
    cars_count = 0

    def __init__(self, wheels_count, sits, guns_count):
        Banderomobil.cars_count += 1
        self.wheels_count = wheels_count
        self.sits = sits
        self.guns_count = guns_count
    
    @staticmethod
    def print_info(self):
        infoString = "Бандеромобіль на {} колесах, призначений для {} людей і {} стволів"
        print(infoString.format(
                self.wheels_count,
                self.sits, 
                self.guns_count))


car1 = Banderomobil(wheels_count, sits, guns_count)
car1.print_info(car1) 
print(car1.cars_count)

car2 = Banderomobil(wheels_count+1, sits+1, guns_count+1)
# car2.print_info()
print(car2.cars_count)