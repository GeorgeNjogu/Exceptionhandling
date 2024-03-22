try:
  print()
except:
  print("An exception occurred")
else:
    print("No exception occurred")
finally:
      print("Finished")

#Classes in python
#A class is an object constructor,or a "blueprint" for creating objects

class Student:
    student_id = 0
    student_name = ''
    student_age = 0
    def __init__(self,student_id,student_name,student_age):#__init is a constructor
        self.student_id = student_id
        self.student_name =student_name
        self.student_age =student_age

    def displayStudent(self):
        print("The student details are:Name:",self.student_name,"Age:",self.student_age)











