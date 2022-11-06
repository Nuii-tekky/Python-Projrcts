#User input can be gotten using the input function
#then you have to print it


print(input('enter any thing you wanna: '))

#Here we've used input function in this length function 

def length(unit):
    if unit<10:
        return 'short'
    elif unit==20:
        return 'cool'
    else:
        return 'too long'
    
user_text= float( input('enter a suitable length: ') )   
print(length(user_text))

#to include the user's input in the the output we use a special string formatting

user_input= input('enter a wrestler: ')

message='%s is not a good wrestler' % user_input

print(message)

#--------------------------------------------------------------------------

name= input('Please insert your first-name: ')
surname= input('Please insert your last-name: ')
hobby= input('Whats your hobby?: ')
status= input('spell the word \'animal\': ')

message= 'Hi there %s %s ,you obviously like %s and thats because you are an %s' %(name,surname,hobby,status)

print(message)

#to take it a notch more ,lets create a function with if statements 

text= input('enter a word: ')
message_1= '%s is to long,try again ' % text
message_2= '%s is to short,try again ' % text
message_3= '%s is okay ' % text

def notch():
    if len(text)<7:
        return message_2
    
    elif len(text)==9:
        return message_3
    
    else:
        return message_1
    
print(notch())    