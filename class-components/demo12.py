import sys

s1='hello world'
s2='hi world'
s3='hi world'
s4='hi world'
print(sys.getrefcount(s4))
print(sys.getrefcount('hi world'))
print(sys.getrefcount('hello world'))


