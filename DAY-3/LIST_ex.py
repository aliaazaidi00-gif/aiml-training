# print("List Example One")

# my_list = [10,20,30, "Python",None,True,12,45, 'Alia']
# print('Number of items in list are:',len(my_list))          #function len untuk totalkan number dalam number list

# for item in my_list:
#     print(item)

#DIA PRINT ONE BY ONE
# print("Second example of list")
# emps=["Conrad,","Belly","Jeremiah","Steven"]
# print("Number of Employees",len(emps))
# print('All Employees')
# for emp in emps:
#     print(emp)

#NAK JADIKAN EMP ONE LINE
# print("Second example of list")
# emps=["Conrad","Belly","Jeremiah","Steven","Taylor","Denise"]
# print("Number of Employees",len(emps))
# print('All Employees')
# for emp in emps:
#     print(emp,end=" ")

# #SORT EXAMPLE (ASCENDING ORDER) 
# #listName.sort()
# emps.sort()
# print("list after sorting")
# for e in emps:
#     print(e, end=" ")

# #SORT EXAMPLE (DESCENDING ORDER)
# #listName.reverse()
# emps.reverse()
# print('Employees in descending order')
# for e in emps:
#     print(e, end=" ")

# print (emps)
#append,remove,pop insert method

emps=["Conrad","Belly","Jeremiah","Steven","Taylor","Denise"]
print("Number of Employees",len(emps))
for emp in emps:
    print (emp,end=" ")

#     #append: add the item at the end of the list
# newEmp=input("\nEnter employee name to add in list:\t")    #to add item in the current list
# emps.append(newEmp)
# print('\nAfter adding new employee: Number of employees are',len(emps))
# for emp in emps:
#     print(emp,end=" ")

#insert(index,item): this will add item at given index
# newEmp=input("\nEnter employee name to add in list:\t")   
# pos=int(input("Enter position where you want to insert inside list "))       #guna integer sebab number 
# emps.insert(pos,newEmp)
# print('\nAfter adding new employee: Number of employees are',len(emps))
# for emp in emps:
#     print(emp,end=" ")

#listName.remove(item): Will remove item from the list
# delEmp=input('\nEmployee to remove from the list:\t')
# emps.remove(delEmp)
# print(f"Number of Employees after deleting {delEmp} in list are",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#IF THE ITEM ISNT IN THE LIST
delEmp=input('\nEmployee to remove from the list:\t')
if delEmp in emps:
    emps.remove(delEmp)
    print(f"Number of Employees after deleting {delEmp} in list are",len(emps))
    for emp in emps:
     print(emp,end=" ")
else: 
   print(f'no such item {delEmp} in employee list')          #this will 
   
# #POP() EXAMPLE             #pop-delete
# emps=["Conrad","Belly","Jeremiah","Steven","Taylor","Denise"]
# print("\nNumber of Employees",len(emps))
# for emp in emps:
#     print (emp,end=" ")   
 
# del_index=int(input('\nEnter index to pop item'))
# print('Pop Reult: ',emps.pop(del_index))

# print("Number of Employees after pop() are",len(emps))
# for emp in emps:
#     print (emp,end=" ")

#find out first and last element from the list
# emps=["Conrad","Belly","Jeremiah","Steven","Taylor","Denise"]
# print("Number of Employees",len(emps))
# for emp in emps:
#     print (emp,end=" ")

count=len(emps)
print('\n First Element of employees list is: ',emps[0])
print('\n Last Element of employees list is: ',emps[-1])
print('\n Second Last Element of employees list is: ',emps[-2])
print('\n Last Element of employees list is: ',emps[count-1])