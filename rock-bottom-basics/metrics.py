
query= input("hi there do you wanna calculate area of some flat shapes? press 'y' to continue: ")

def myfunc(value):

  def square(para):
    para= int(para)
    return para*para

  def rectangle(para2,para3):
    para2= int(para2)
    para3= int(para3)
    return para3*para2
  
  def circle(para4):
    para4= int(para4)
    return pi*para4*para4

  def triangle(para5,para6):
    para5= int(para5)
    para6= int(para6)
    return (para6*para5)/2

  pi= 22/7
  value= value.lower()
  if value== 'y':
    query_2= input('I can only calculate for square,rectangle,circle,triangle.type the first letter of the one you want! : ')
    query_2= query_2.lower()
    if query_2== 's':
      query3= input('enter the unit: ')
      return square(query3)
    elif query_2== 'r':
      query_4= input('enter the first value: ')
      query_5= input('enter second value: ')
      return rectangle(query_4,query_5)  
    elif query_2== 'c':
      query_6= input('enter the radius: ')
      return circle(query_6)  
    elif query_2== 't':
      query_7= input('enter the height: ')
      query_8= input('enter the base length: ')
      return triangle(query_7,query_8)
    else:
      return 'Invalid Input'  
  else :
    return 'Invalid Input'  

print(myfunc(query))






