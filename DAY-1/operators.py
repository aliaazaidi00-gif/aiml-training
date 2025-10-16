#Assignment operators: =, +=, -=
price=float(input("Enter Product Price"))
discount=price*0.10
disPrice=price-discount 
print(f"Price: {price} \n Discount {discount} \n Discounted Price{disPrice}")

salary=50000.50
bonus=5000.60
print("salary {salary} and bonus {bonus} ")

# salary+=bonus   #salary=salary+bonus
# print("salary with bonus",salary)

# salary=50000.50
# tds=salary*0.10
# print(f"salary {salary} and TDS {tds}")

# salary-=tds     #salary=salary-tds
# print("Salary after tax", salary)

#comparison operators: ==, >, >=, <, !+ etc.

# if(condition)
# code
# else
# code

# age=int(input("Enter Your age"))
# if(age>=18):
#     print("you are eligible to cast your vote")
# else:
#     print("you are not eligible to cast your vote, you have to wait")

# print("End of program")

# marks=int(input("Enter marks percentage without percent '%' sign"))
# if(marks<30):
#     print("Fail in exam")
# else:
#     print("clear th exam")


#accessCode="wes12"

# !means not equal to
# accessCode=input("Enter access code")
# if(accessCode!="wes12"):
#     print("invalid access code")
# else:
#     print("welcome to your course")

# == means equal
# accessCode=input("Enter access code")
# if(accessCode=="wes12"):
#    print("welcome to our courses")
# else:
#     print("invalid access code")

#logical operators: and, or, not
# physicMarks=int(input("Enter makrs obtained in Physics: "))
# cheMarks=int(input("Enter maarks obtained in Chemistry: "))
# mathMarks=int(input("Enter marks obtained in Mathematics: "))

# if((mathMarks>=50) and (physicMarks>=55) and (cheMarks>=60)):
#     print("you are eligible to sit in pre exam of MBBS")
# else:
#     print("you have not got the required marks")

# idProof=input("Enter ID proof you have: \t")
# if((idProof=="passport")or(idProof=="dl")or(idProof=="voter id")):
#     print(f"valid ID {idProof} we acccept here")
# else:
#     print("only passport,dl and voter id are accepted as Identify Proof")
#     print(f"{idProof}:is not valid ID here")

# MathMarks=int(input("Enter makrs obtained in Mathematics:\t"))
# gapYear=int(input("Enter Year gap if any otherwise zero :\t"))
# if((MathMarks>=55) or (gapYear!=0)):
#    print("Not eligible for BTech")
# else:
#    print("Eligible for BTech")

# name=input("Enter User Name")
# if(not name):
#     print("Error!!!")
# else:
#     print("Welcome", name)
