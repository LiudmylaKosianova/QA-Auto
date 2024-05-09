class ShopWorker:
    count_workers = 0

    def __init__(self, name1="", age1=0):
        self.name = name1
        self.age = age1
        ShopWorker.count_workers += 1
        self.id = ShopWorker.count_workers

    def add_year(self, year):
        self.age += year

    def __str__(self):
        str_out = "Працівник " + str(self.id) + ": " + self.name + " " + str(self.age)
        str_out += " всіх працівників " + str(ShopWorker.count_workers)
        return str_out

    @staticmethod
    def info():
        print("В магазині працює: ", ShopWorker.count_workers, " працівників")

    @classmethod
    def naming_shop(cls, name):
        cls.name_shop = name
        return cls.name_shop


ShopWorker.info()
worker_one = ShopWorker("Іван", 25)
print(worker_one)
worker_one.add_year(3)
print(worker_one)
worker_two = ShopWorker("Петро", 32)
print(worker_two)
worker_two.add_year(2)
print(worker_two)
print("Назва магазину: ", worker_one.naming_shop("Fara"))
print("Назва магазину: ", ShopWorker.name_shop)
print("Назва магазину: ", ShopWorker.naming_shop("Para"))
