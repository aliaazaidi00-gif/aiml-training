numbers = [10, 25, 40, 40, 2, 1]
double_num= list(map(lambda x: 2*x, numbers))
print('\noriginal list')
for num in numbers:
    print(num, end=" ")

print('\n\nDouble list')
for num in double_num:
    print(num, end=" ")
print()
