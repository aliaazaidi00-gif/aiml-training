import math
import inspect
# num=int(input('\nEnter number to find square root\t:'))
# print(f'Square root of {num}\t\t\t:',round(math.sqrt(num),2))
# print()

functions = inspect.getmembers(math, inspect.isbuiltin) 
print('All functions in math module')
for n, func in functions:
    print(n,end="\t")

