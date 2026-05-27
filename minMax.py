minMaxList = [3,5,6,77,3,55,33,7,2]

smallest = minMaxList[0]
largest = minMaxList[0]

for i in range(len(minMaxList)):

    if minMaxList[i] > largest:
        largest = minMaxList[i]

    if minMaxList[i] < smallest:
        smallest = minMaxList[i]

print("min is :", smallest, "max is :", largest)