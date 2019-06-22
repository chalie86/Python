
try:
    a = int("1233rre4")
    print("The program is hear")
except ValueError:
 print("An error occurred")

 print("The program is finished")

 try:
     num1 = int(input("Enter the first number"))
     num2 = int(input("Enter second number"))
     print (num1 / num2)
 except ZeroDivisionError:
     print("Any number cannot be dividend by zero,please enter correct number ")
 except ValueError:
     print("Enter invalid for the conversion! Please check your value ")
 else:
      if (num1 < 0 or num2 < 0):
          print("Negative number is entered")
finally:
   print("this statement will always be executed")
print("the program has finished")



def sqrt(num):
    if(num <= 0 ):
        raise ValueError("You should write a positive number")
    else:
        return num  ** 00.5
