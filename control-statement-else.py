number1 = int(input("Enter number 1"))
number2 = int(input("Enter number 2"))
number3 = int(input("Enter number 3"))
max = 0
if( number1 > number2 and number1 > number3) :
    max = number1

else :
    if( number2 > number1 and number2 > number3) :  
         max = number2
     
    else : 
        max  = number3
 
print('max of three numbers is ',max)