listlist = []
listsub = 0 
listtot = 0 
for x in range(0,100,3):
    print(x)
    listsub = listsub + 1
    listlist.append(listsub)
    listtot = listtot + listsub
print(listsub)

sumx = sum(listlist)
print('summed total =', sumx)
print('my total = ', listtot)
