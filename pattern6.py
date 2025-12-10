# pattern to print 
# 1
# 1 0 
# 1 0 1 
# 1 0 1 0
# 1 0 1 0 1


n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(' ', col,end='')
    print('')
    