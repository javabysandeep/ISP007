from functools import reduce

names = {"shubham1": 23,
         "shubham2": 21,
         "hanumant": 20,
         "aamar":20, "swagat":21, "sahil1":20, "sahil2":32, "madhavi":22, "bhakti":18}
result = 0
for key,value in names.items():
    if key in names:
        result += value
print(result//len(names))

r = reduce(lambda x,y:x+y,names.values())
print(r//len(names))