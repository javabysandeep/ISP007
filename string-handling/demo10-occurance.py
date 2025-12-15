str = 'good morning'
map = {}
for ch in str:
    if ch in map.keys():
        map[ch] += 1
    else:
        map[ch] = 1

for item in map.items():
    print(item)
