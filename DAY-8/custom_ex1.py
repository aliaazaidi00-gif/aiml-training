class InvalidAge(Exception):
    pass
def check_age(age):
    if (age<=0):
        raise InvalidAge("Age cannot be negative")
    if(age<18):
        raise InvalidAge("Age less than 18 not allowed")
    elif (age>=80):
        raise InvalidAge("Too old to work") 
    else:
        print(f'Age {age} is accepted and valid age for employment')
try:
    userage=int(input("Enter your age: "))
    check_age(userage)
except InvalidAge as e:
    print("Invalid Age:",e)
except Exception as ex:
    print("Error Occured:",ex)
