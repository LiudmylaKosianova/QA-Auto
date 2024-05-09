class Dog:
    def __init__(self, age=0, name="Jack"):
        self.age = age
        self.name = name

    def print_Name(self):
        print(f"Значення поля name = {self.name} .")


d1 = Dog("", 12.5)
d1.print_Name()
