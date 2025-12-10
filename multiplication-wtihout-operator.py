number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
#print(number1 * number2)
# 5 * 4 = 20 ---> [5+5+5+5] --> [4 + 4 + 4 +4 +4]
result=0
for i in range(1,number1+1):
    result = result + number2
    
print(result)



