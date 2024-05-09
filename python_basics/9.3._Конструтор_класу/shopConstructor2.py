class ShopWorker:
    count_workers = 0

    def __init__(self, name1="", age1=0):
        self.name = name1
        self.age = age1
        ShopWorker.count_workers += 1


print("всіх працівників ", ShopWorker.count_workers)

worker_one = ShopWorker()

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

worker_three = ShopWorker("Семен")

print(
    "Працівник 3: ",
    worker_three.name,
    " ",
    worker_three.age,
    " всіх працівників ",
    worker_three.count_workers,
)
