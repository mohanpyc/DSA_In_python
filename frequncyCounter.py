toBeC=["a", "b", "a", "c", "b", "a"]
frequency={}

for item in toBeC:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

print(frequency)