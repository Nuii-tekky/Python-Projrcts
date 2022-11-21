

#if statements are called conditionals because they give python a certain function to carry out at a certain time or when the condition says so.


if 3>1:
    print('yay,i\'m python')
else:
    print('nay i\'m pythax')


#modified mean program

def mean(input):
    if type(input)== dict:
        mymean=sum(input.values())/len(input)
    else:
        mymean=sum(input)/len(input)    
    return f'The mean is {mymean}'

students_grades={'mary':30,'joe':45,'paul':50,'james':49,'edward':39}
students_scores=[23,26,27,36,38,38,39,29.92]

print(mean(students_grades))
print(mean(students_scores))