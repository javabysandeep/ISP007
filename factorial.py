# find the factorial of a given number
number = int(input("Enter a number"))
# e.g. 5! = 1 * 2 * 3 * 4 *5 or 5!= 5*4*3*2*1 => 120
result=1
for i in range(1, number+1):
    result = result * i
    
print('factorial is ',result)