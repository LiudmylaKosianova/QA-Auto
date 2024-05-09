number = int(input())
myDict = dict()
for i in range(number+1):
    key = i
    value = i*i
    myDict[key] = value
print(myDict)