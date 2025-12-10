#range of prime numbers
for number in range(1,1000):
    isPrime=True
    i=2
    while(i<=number//2):
        if(number%i==0):
            isPrime=False
            break
        i=i+1

    if(isPrime) :
        print('prime number =',number)




