class ShopWorker:
    pass


worker_one = ShopWorker()
worker_two = ShopWorker()

worker_one.name = "Іван"
worker_one.age = 25

worker_two.name = "Петро"
worker_two.age = 32

print("Працівник 1: ", worker_one.name, " ", worker_one.age)
print("Працівник 2: ", worker_two.name, " ", worker_two.age)
