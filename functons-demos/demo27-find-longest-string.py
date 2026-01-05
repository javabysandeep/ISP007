from functools import reduce

names=["Madhavi","Amar","Swagat","Sahil","Shubham","Hanumant"]
#longest String using map-filter-reduce

print(reduce(lambda a,b: a if len(a)>len(b) else b,names))