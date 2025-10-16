# numbers = [10, 25, 40, 40, 2, 1]

# print('\noriginal list')
# for num in numbers:
#     print(num, end=" ")

# even_numbers=list(filter(lambda x: x%2==0,))

# print('\neven Numbers from list as follows\n')
# for num in even_numbers:
#     print(num, end=" ") 

#you have following list
# our_list=[4,2,5,6,7,3,1,10]
#  #Write code using filter to find out all the number less than 5
#  #  from the list

# our_number=list(filter(lambda x: x<5, our_list))

# print('\noriginal list:')
# for num in our_list:
#     print(num, end=" ")

# print('\n\nNew list as follows:\t')
# for num in our_number:
#     print(num, end=" ")
# print()
# print()

students_marks={'Alia':12,
                'Syahmi':90,
                'Nadia':81,
                'Shayangku':61,
                'Akif':39,
                'Odah':20,
                'Nurul':100
                }
print('\nAll Students:')
print(students_marks)
pass_students=dict(filter(lambda i:i[1]>=40, students_marks.items()))                
print("\nPassed Students:", end=(""))
print(pass_students)
print()

print('\nAll Students:')
for k,v in students_marks.items():
    print(f'Name: {k} -> Marks {v}')                                                            #k is name, v number

pass_students=dict(filter(lambda i:i[1]>=40, students_marks.items()))                           #ada filter untuk tunjuk passed je

print('\nPassed Students')
for k,v in pass_students.items():
    print (f'Name: {k} -> Marks {v}')

sort_pass_students=dict(sorted(pass_students.items(), key=lambda x: x[1]))            
print('\nAscending Order')
for k,v in pass_students.items():
    print (f'Name: {k} -> Marks {v}')

sort_pass_students_desc=dict(sorted(pass_students.items(), key=lambda x: x[1], reverse=True))
print('\nDescending Order')
for k,v in pass_students.items():
    print (f'Name: {k} -> Marks {v}')
print()

