#dictionaries are similar to lists in layout but not in syntax
#they have to have keys and values
#they are dclared by using curly brackets {}and the contents seperated by commas


mydict={'cool': 'dog','yummy': 'chicken','wild': 'baboon'}
print(mydict)

#list items can be called on by indexes,dictionary items are accessed by their keys
print(mydict['cool'])
print(mydict['yummy'])
print(mydict['wild'])

eng_efik={'akpan':'firstborn','ndidia':'food','uwem':'life','ewa':'dog'}
print('what is akpan:',eng_efik['akpan'])
print('what is ndidia:',eng_efik['ndidia'])
print('what is uwem:',eng_efik['uwem'])

#we can also get the values of the dictionary items using the value function

print(mydict.values())
print(type(eng_efik),type(type))