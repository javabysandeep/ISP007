str = 'abcaabcdd'
# output = abcd
set={}
for i in str:
    set.setdefault(i,0)
print(''.join(set.keys()))

