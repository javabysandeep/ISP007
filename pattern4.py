# pattern to print 

#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5


n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row,end='')
    print('')
    