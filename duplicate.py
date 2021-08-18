listing = [ 2,5,6,7,9,7,5]
uniq = []
for item in listing:
    if item not in uniq: 
        uniq.append(item)

print(uniq)