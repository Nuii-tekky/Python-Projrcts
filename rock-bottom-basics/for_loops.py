#for loops are one of the powerful loops in python

#lets loop around every item in the following list

mylist=[8,1,2,3,4,5,6,7,8,9,10,19,18,17]

for item in mylist:
    print(item)
    
mytext=['sam','paul','david','bassey','killerbean','sofia','amber','james',]

for item in mytext:
    print(item)

#now lets 'for loop' around a dictionary

mydict={'nigeria': 10,'ghana': 40,'benin': 83,'mauritus': 38,'sri lanka': 99}


for country in mydict.keys():
    print(country)
    
for number in mydict.values():
    print(number)    