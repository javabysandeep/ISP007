# pattern to print 

#* * * * *
#* * * *
#* * *
#* *
#*

row=5

while(row > 0):
    col=1
    while(col <=row):
        print('*', end='')
        col =col+1
    print('')
    row =row-1
