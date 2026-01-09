import random
names=["shubham1","shubham2","hanumant","aamar","swagat","sahil1","sahil2","madhavi","bhakti"]
print(random.choice(names))
print(list(filter(lambda x:x.startswith("s"),names)))


