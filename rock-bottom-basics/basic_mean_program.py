#since theres is no function to find mean in python
#i'm gonna use a shortcut
#i'll find the sum of the numbers and the number of scores with functions that are in python.

students_scores=[45,35,60,56,34,56,40,23,45,46,67,73,37,4,23,58,27,64]
sum_of_scores=sum(students_scores)
number_of_scores=len(students_scores)

mean= sum_of_scores/number_of_scores
print(mean)