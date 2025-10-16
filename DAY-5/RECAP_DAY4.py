def display():
    print('\nWelcome to the recap of functions')

def welcome(name):
    print('\nWelcome to functions Mr.\\Ms. Alia', name)

def cube(num):
    cube_num=num*num*num
    print(f'Cube of given number: {num} is =\t{cube_num}')

def square(num):
    return num*num                    #if nak return the value 

# welcome('Alia')
# display()
my_num=int(input('Enter Number to find out Cube:\t'))
cube(my_num) 

username=input('Enter Username: \t')
my_num=int(input('Enter number to find out cube and square: \t'))

welcome(username)
cube(my_num)
sqnum=square(my_num)
print(f'Square of {my_num} is: {sqnum}')
print(f'Number: of {my_num} square: {sqnum}')
