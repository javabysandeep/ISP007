s = {}
print(type(s))  # dict
s = {1, 2, 3, 4, 4, 5}
print(type(s))
print(s) # {1, 2, 3, 4, 5}
print("length is ",len(s))
s.add(99)
print(s)
s.update([91,92,97,98])
print(s)
q= s.copy()
print(q)
q.pop()
q.pop()
q.pop()
print(q)
q.remove(4)
q.discard(4)
print(q)
q.clear()
print(q)
