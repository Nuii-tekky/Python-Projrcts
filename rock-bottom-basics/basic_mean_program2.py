#the predecessor of this file was made with a list which is not appropriate with the kind of data we put in.
#since we are putting in students scores we have to have some kind of identity to those values.
#we can do that with a dictionary instead of list.

#dictionary unlike lists is declared with a curly bracket{}
students_scores= {'troy': 34,'matt': 47,'dabad': 64,'kim':59,'finn': 46}

sum_of_scores=sum(students_scores.values())
number_of_students=len(students_scores.keys())

mean=sum_of_scores/number_of_students


print('Here\'s is the student mean :',mean)
