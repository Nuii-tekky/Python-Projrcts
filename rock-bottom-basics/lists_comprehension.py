#using floatdata types in large sites is not storage friendly
#dats why we use lists comprehension to solve that

mylist=[123,234,456,678,878,765,456,456,329,494,423]

#what i want here is a list with float data types but instead  i use whole nmbers 

#my desired list is:[12.3,23.4,45.6,67.8,87.8,76.5,45.6,45.6,32.9,49.4,42.3]

#so what i'll do is use a for loop to iterate round the items and divide it by 10,then add it to a new empty variable

new_list=[]

for item in mylist:
    new_list.append(item/10)    

print(new_list)

#the above method has now been replaced by a shorter syntax

new_list=[item/10 for item in mylist]
print(new_list)