
# ##a casual program 
# ##its tell you an input is even or odd number

# #while True:
# #    number= float(input('enter a number: '))
# #    if number % 2==0:
# #        print('thats an Even number congrats!','try again')
# #    else:
# #        print('thats an Odd number, Try again')
        

# #another casual program to calculate area of square and rectangle
        
# def square(a):
#     return a*a    

# def rect(a, b):
#     return a*b    

# while True:
#     user_input= input('Area of square or rectangle? Type s or r: ')
#     if user_input== 's':
#         print('the area is :',square(float( input('enter a value: '))))
#     elif user_input== 'r':
#         print('the area is :',rect(float( input('enter the values:  ').split())))    
        
# #how to prompt user input to accept two arguments        


numbers= [1,2,3,4,5,6,7,8,9,10]

start=0

for number in numbers:
  start+=number
print(start)
