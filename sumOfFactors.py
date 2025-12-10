#find the sum of factors of given number and check if it is perfect or not
# 6 = 1,2,3 --> these numbers are called as factors of 6
# 12 = 1,2,3,4,6 
number=int(input('Enter the number'))
sum=0
for i in range(1, number//2 +1) :
    if(number%i==0):
        print(i)
        sum = sum + i


print('sum of factors ',sum)

# number is called perfect if the sum of its factors is equal to given number
# 28 is a perfect number = 1 +2 + 4 +7 +14
if(sum==number):
    print('its perfect number')
else :
    print('not a perfect number')