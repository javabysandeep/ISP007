a = [2,3,4,6,5]
print(a)
left = 0
right = len(a)-1
while left < right:
	temp = a[left]
	a[left]= a[right]
	a[right]=temp
	left +=1
	right -=1
print(a)


a = [2,3,4,6,5]
max = -1
smax = -1
for num in  a:
	if num > max:
		max = num
	if num > smax and num < max:
		smax = num
print(max)
print(smax)