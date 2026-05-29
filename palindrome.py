text = 'radar'
num = 1221

isTextSame=""
isNumSame=0

copyNum=num

for i in range(len(text)-1,-1,-1):
    isTextSame+=text[i]

print(isTextSame==text,"if ture its a palindrome")

while copyNum>0:
    isNumSame=isNumSame*10+copyNum%10
    copyNum=copyNum//10

print(isNumSame==num,"if true its a palindrome")