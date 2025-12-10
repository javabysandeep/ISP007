#find the factors of given number
# 6 = 1,2,3 --> these numbers are called as factors of 6
# 12 = 1,2,3,4,6 
number=int(input('Enter the number'))
for i in range(1, number//2 +1) :
    if(number%i==0):
        print(i)

