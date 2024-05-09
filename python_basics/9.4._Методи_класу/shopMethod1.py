class ShopWorker:
    count_workers = 0

    def __init__(self, name1="", age1=0):
        self.name = name1
        self.age = age1
        ShopWorker.count_workers += 1

    def add_year(self, year):
        self.age += year


print("всіх працівників ", ShopWorker.count_workers)

worker_one = ShopWorker("Іван", 25)
print(
    "Працівник 1: ",
    worker_one.name,
    " ",
    worker_one.age,
    " всіх працівників ",
    worker_one.count_workers,
)
worker_one.add_year(3)
print(
    "Працівник 1: ",
    worker_one.name,
    " ",
    worker_one.age,
    " всіх працівників ",
    worker_one.count_workers,
)

worker_two = ShopWorker("Петро", 32)
print(
    "Працівник 2: ",
    worker_two.name,
    " ",
    worker_two.age,
    " всіх працівників ",
    worker_two.count_workers,
)
worker_two.add_year(2)
print(
    "Працівник 2: ",
    worker_two.name,
    " ",
    worker_two.age,
    " всіх працівників ",
    worker_two.count_workers,
)
