number = int(input("Enter a number"))
# prime number : number is only divisible by 1 and number itself.
# e.g. 2,3,5,7, 11, 13, 17, 19, 23, 29
# 50 --> 25, 100 --> 50, 500 ---> 250, 1000-> 500
# for the given number the maximum divisor is n/2
# maximum factor n/2
# 6 = 1,2,3,  10=1,2,5, 16=1,2,4,8 --> 20=1,2,4,5,10 --> 17= 2 to n/2
# range = 2 to n/2 
# will assume number is prime  isPrime = True
isPrime=True
i=2
while(i<=number//2):
    if(number%i==0):
        isPrime=False
        break
    i=i+1

if(isPrime) :
    print('its prime number')
else :
    print('not a prime number')



