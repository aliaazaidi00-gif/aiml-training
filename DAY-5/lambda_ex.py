# def add(a,b):
#     total=a+b
#     return total

# result=add(12,15)
# print(result)

addition=lambda a, b: a + b                             #can put as many as you want 
multi=lambda a,b: a*b
div=lambda a,b: a/b
avg=lambda a,b: (a+b)/2
sub=lambda a,b:(a-b)

num1=int(input('Enter first number\t\t\t\t:\t'))
num2=int(input('Enter second number\t\t\t\t:\t'))

print('multiplication result\t\t\t\t:\t', multi(num1,num2))
print('subtraction result\t\t\t\t:\t', sub(num1,num2))

#LAMBDA EXAMPLE TO FIND OUT ODD OR EVEN NUMBER

check_odd=lambda n:"Odd Number" if n%2==1 else 'Even Number'
num1=int(input('Enter Number to check Odd or Even: \t')) 
print(check_odd(num1))
