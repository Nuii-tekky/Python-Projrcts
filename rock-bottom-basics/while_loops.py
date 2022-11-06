##while loops are more powerful and are used differently
##its works on a given condition


#a=19

#while a>10:
#    print('a is greater than 10')    
##this would literally go on forever in the terminal    
    
    
#lets write a more efficient use for while loops

while True:
    number=int(input('enter a number: '))
    message_1='%s is too small' % number
    message_2='%s is too big' % number
    message_3='%s is just Righhht' % number
    
    if number<34:
        print (message_1)
    elif number>35:
        print (message_2)
    else:
        print (message_3)
    

    