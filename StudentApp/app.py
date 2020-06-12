student_list = []

class Student:
  def __init__(self,name):
     self.name = name
     self.mark = []

  def average_mark(self):
       number = len(self.mark)
       if number == 0:
        return 0



def create_student():
    name = input("Please enter the new student name: ")
    student_data = Student(name)


    return student_data

    s =  create_student()

def add_mark(student,mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    total = sum(student.marks)
    number = len(student.marks)
    if number == 0:
        return 0
    total = sum(student.marks)
    return total / number

def student_details(student):
    print("{},average mark: {}.".format(student.name,
                                        student.average_mark()))


def print_student(student_list):
    for students in student_list:
        student_details(students)

def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'S' to add new student, "
                      "'a'to add a to a student, "
                      "or 'q' to quite .")
    while selection != 'q':
      if selection == 'p':
         print_student(student_list)
      elif selection == 's':
            student_list.append(create_student())
      elif selection ==  'a':
            student_id = int(input("Enter the student id to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student,new_mark)

      selection = input("Enter 'p' to print the student list, "
                      "'S' to add new student, "
                      "'a'to add a to a student, "
                      "or 'q' to quite .")

menu()


