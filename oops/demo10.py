import gc

s1='hello world'
s2='hi world'
s1=s2
print(s1)
print(s2)
# hello world is an unreferenced object i.e. Garbage
print(gc.isenabled())
