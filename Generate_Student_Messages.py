#Lesson 6: Scripting with Raw Input
names = input("Enter the student names separated by commas: ").split(',') # get and process input for a list of names
assignments =  input("Number of missing assignments separated by commas: ").split(',')# get and process input for a list of the number of assignments
grades =  input("The current grade separated by commas: ").split(',')# get and process input for a list of grades
grades_updated = []

print(grades)
# message string to be used for each student

# HINT: use .format() with this string in your for loop
#message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
#submit before you can graduate. You're current grade is {} and can increase \
#to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(names)):
    print(i)

    grades_updated.append(str(float(grades[i]) + 2*float(assignments[i])))
    message = """Hi {},\n\nThis is a reminder that you have {} assignments left
    to submit before you can graduate.
    You're current grade is {} and can increase to {}
    if you submit all assignments before the due date.\n\n"""

    #print(grades_updated[i])
    print(message.format(names[i], assignments[i], grades[i], grades_updated[i]))
