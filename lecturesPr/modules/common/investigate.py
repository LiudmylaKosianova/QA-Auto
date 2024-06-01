import sqlite3

connection = sqlite3.connect(r"/home/carmin/Public/QA-Auto/project_lectures"+r"/become_qa_auto.db")
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(tables)