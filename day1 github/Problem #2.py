#import the collection package
import collections
#example hardcore value
name = ["rajesh", "siva", "malkkar", "nithish", "vasanth", "kaveri"]
mark = [55, 45, 65, 34, 78, 66]
#intilize the an list and failcount is 0
pass_student = []
fail_count = 0
#check the mark until length of name list
for i in range(len(mark)):

    #mark is greater than 50 append into pass_student list else count fail
    if mark[i] > 50:
        pass_student.append(f"{name[i]}:{mark[i]}")
    else:
        fail_count += 1

print(pass_student)
print(fail_count)


