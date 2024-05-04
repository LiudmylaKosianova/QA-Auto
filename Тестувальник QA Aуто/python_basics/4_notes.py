myList = [45, 998, 11]
print(myList)
myList.append(33)
print(myList)
myList[0] = 175
del myList[2]
myList.remove(17)

n = 4
gasList = []
for i in range(n):
    number = float(input("number: "))
    gasList.append(round(number, 3))

for element in gasList:
    print(element)
