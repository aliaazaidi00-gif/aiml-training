# #default parameter in functions
# def info(ID,Name,City="KL"):
#     print(f'\n\nDetails as follows \n ID:\t {ID} \n Name:\t {Name} \n City:\t {City}')

# info(1, "Alia","Kuala Lumpur")
# info(101,"Syahmi")
# info(103,"Arab")

# #we want to create a single methof that can able to add 2 numbers, 3 numbers,4 numbers or numbers
# # #and return correct total

# def add(n1,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4

# print("Result: ",add(1,2))
# print("Result: ",add(5,3,1,4,10))
# print("Result: ",add(5,25,10))

# def add(*nums):
#     return sum(nums)

# print('sum of 1,10,11 is: \t\t',add(1,10,11))
# print('Sum of 5,2 is: \t\t\t',add(5,2))
# print('sum of 10,100,400,300,450 is: \t',add(10,100,400,300,450))

# print('Maximum Example')
# print('Maximum of 1,10,11 is: \t',max(1,10,11))
# print('Maximum of 6,9,7 is: \t',max(6,9,7))
# print('Maximum of 8,3,1,5 is: \t',max(8,3,1,5))

# print('Minimum Example')
# print('Minimum of 1,10,11 is: \t',min(1,10,11))
# print('Minimum of 6,9,7 is:\t',min(6,9,7))
# print('Minimum of 8,3,1,5 is: \t',min(8,3,1,5))
