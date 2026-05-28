toBeReversed = 'string'

reversedString = ''

for i in range(len(toBeReversed)-1,-1,-1):
    reversedString+=toBeReversed[i]

print(reversedString)