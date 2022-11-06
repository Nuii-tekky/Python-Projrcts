

# who knew python has feelings

main_query= input('I dare you to type: \'python is trash\': ')


def interprete(word):
  word= word.lower()
  if word== 'python is trash':
    query_2= input('uhmm am being used by 20million developers at this instant,how cool are you??: ').lower()
    if query_2=='very cool':
      return 'go and have a rest and think deeply about what you just said '
    elif query_2== 'so cool':
      return 'hahaha dont crack me up,you couldn\'t be cool even if you were forced to '  
    else:
      return 'i dont have your time abeg '
  else:
    return 'mumu is that what i asked you to type?? '    

print(interprete(main_query))  


