class ShopWorker:
    count_workers = 2


worker_one = ShopWorker()
worker_two = ShopWorker()

worker_one.name = "Іван"
worker_one.age = 25

worker_two.name = "Петро"
worker_two.age = 32

print(
    "Працівник 1: ",
    worker_one.name,
    " ",
    worker_one.age,
    " всіх працівників ",
    worker_one.count_workers,
)
print(
    "Працівник 2: ",
    worker_two.name,
    " ",
    worker_two.age,
    " всіх працівників ",
    worker_two.count_workers,
)
print("всіх працівників ", ShopWorker.count_workers)
