# print tables from 1 t0 30
for row in range(1,11):
    for col in range(1,31):
        print(' ',col * row,end='')
    print()