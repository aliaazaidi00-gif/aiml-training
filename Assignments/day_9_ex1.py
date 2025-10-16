#write a program using functions to find greatest of three numbers entered by user.
#write the solution in Assignments folder of your with name (day 9_Ex.py).
#push on GitHub.
#share GitHub link in chat once done.

def greatest_number(max):
    return max
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
max=num1
if num2>max:
    max=num2
if num3>max:
    max=num3
print("Greatest number is: ",greatest_number(max))
