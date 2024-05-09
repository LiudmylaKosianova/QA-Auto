class ShopWorker:
    _count_workers = 0

    def __init__(self, name1="", age1=0):
        self.name = name1
        self.__age = age1
        self.setting_id()

    def setting_id(self):
        ShopWorker._count_workers += 1
        self.id = ShopWorker._count_workers

    def add_year(self):
        self.__age += 1

    def __str__(self):
        str_out = "Працівник " + str(self.id) + ": " + self.name + " " + str(self.__age)
        str_out += " всіх працівників " + str(ShopWorker._count_workers)
        return str_out

    @staticmethod
    def info():
        print("В магазині працює: ", ShopWorker._count_workers, " працівників")

    @classmethod
    def naming_shop(cls, name):
        cls.name_shop = name
        return cls.name_shop

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age


ShopWorker.info()

worker_one = ShopWorker("Іван", 25)

print(worker_one.get_age())
worker_one.set_age(-44)
print(worker_one.get_age())
ShopWorker.naming_shop("Fara")
print("Назва магазину: ", ShopWorker.name_shop)
