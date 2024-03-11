#In your college Python is taught in 3 different departments by the same professor. 
#For each dept, get the no of students studying Python and their marks in the final exam 
#Get the input as comma seperated string

#Find the top 3 marks in each class
#Find the top 3 marks in all classes are combined.
#Find the avg mark of students with passing mark in each class and the classes combined.
#Find which class has the best average mark and least number of failed students.
def departmentData():
    departments = []
    for i in range(0,3):
        num_students = int(input(f"Enter number of students for Department {i+1}: "))
        marks_input = input(f"Enter marks for {num_students} students: ")
        marks_list = marks_input.split(',')
        marks = []
        for mark_int in marks_list:
            mark = int(mark_int)
            marks.append(mark)
        
        departments.append(f"num_students: {num_students}, marks: {marks}")
    return departments

departments = departmentData()
print(departments)
