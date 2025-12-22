a = ()
print('type of {} is {}'.format(a, type(a)))  # tuple

b = 10, 20
print('type of {} is {}'.format(b, type(b)))  # tuple

c = 10
print('type of {} is {}'.format(c, type(c)))  # int

d = 10,
print('type of {} is {}'.format(d, type(d)))  # tuple

e = (10)
print('type of {} is {}'.format(e, type(e)))  # int

f = (10,)
print('type of {} is {}'.format(f, type(f)))  # tuple

g = (10, 20, 30)
print('type of {} is {}'.format(g, type(g)))  # tuple

x = [1, 2, 3, 4, 5]
y = tuple(x)
print('type of {} is {}'.format(y, type(y)))

y[0]=12 #TypeError: 'tuple' object does not support item assignment
print('type of {} is {}'.format(y, type(y)))