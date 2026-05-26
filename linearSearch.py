listToFind = [1,2,3,4,5,6]
findLocationOf = 5
found = False

for i in range(len(listToFind)):
    if listToFind[i]==findLocationOf:
        print("Location found at :",i)
        found=True
        break

if found is not True:
    print("Location not found")
