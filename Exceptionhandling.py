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

class Student:#classes have properties(features) and behaviours
    student_id = 0
    student_name = ''
    student_age = 0
    def __init__(self,student_id,student_name,student_age):#__init is a constructor where def is the syntax
        self.student_id = student_id
        self.student_name =student_name
        self.student_age =student_age

    def displayStudent(self):#enables you add
        print("The student details are:Name:",self.student_name,"Age:",self.student_age)

student1 = Student(student_id="100",student_name="George",student_age="20")
student2 = Student(student_id="200",student_name="Tom",student_age="18")
student1.displayStudent()
student2.displayStudent()



class Teams:
    team_name = ''
    team_manager = ''
    def __init__(self,name,manager):#one function one print
        self.team_name = name
        self.team_manager = manager
        print("The team details are:name:",self.team_name,"manager:",self.team_manager)

Teams= Teams("Mancity","pep")

#
def getfullname(First,Last):
    z=First+Last+"+254"
    return z
y=getfullname("alex","peters")+"added another thing"
print(y)



#pip is a package manager
#views.py



































