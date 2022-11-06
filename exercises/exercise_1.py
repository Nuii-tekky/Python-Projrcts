#ardit's first exercise trial

#first we define a function to let us format the string beautifully
def sentences(text):
    questions=('how','why','where','when','who')
    upper_case= text.capitalize()
    if text.startswith(questions):
        return '{}?'.format(upper_case)
    else:
        return '{}.'.format(upper_case)

#now we create the looops that keep iterating once the condition is true
#this variable 'final results ' is the output yhat is going to b shownto the user
final_results=[]   
 
while True:
    user_input= input('say something: ')    
    if user_input== 'end':
        break
    else:
        final_results.append(sentences(user_input))
        
print(' '.join(final_results))        
        
        

    
    
    