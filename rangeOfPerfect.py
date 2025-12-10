# range of perfect numbers

for number in range(1,100000):
    sum=0
    for i in range(1, number//2 +1) :
        if(number%i==0):
            sum = sum + i
    if(sum==number):
        print('perfect number = ',number)
