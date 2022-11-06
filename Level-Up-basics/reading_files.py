# python can read files that are called upon

myfile= open('Level-Up-basics/note.txt')

print(myfile.read())

# another way to do this is to use what i like to call a with loop

with open('Level-Up-basics/note.txt') as myfile:
    content=myfile.read()

print(content)    