input_database_name = input("Введіть ім'я бази даних ")
input_command_to_execute = input("Введіть команду для виконання ")


class Database:
    # your code goes here
    executed_commands = []

    def __init__(self, database_name):
        self.database_name = database_name
        self.connected_to_database = False

    @staticmethod
    def to_lower(str):
        return str.lower()

    @classmethod
    def add_to_executed_commands(cls, command):
        cls.executed_commands.append(command)

    def connect_to_database(self):
        self.connected_to_database = True
        print("Під'єднано до бази даних")

    def execute_command(self, command):
        Database.executed_commands.append(command)
        print(command)


db = Database(input_database_name)
print(db.database_name)
print(db.connected_to_database)

db.connect_to_database()
print(db.connected_to_database)
print(Database.executed_commands)

lower_command = Database.to_lower(input_command_to_execute)
db.execute_command(lower_command)
print(Database.executed_commands)
