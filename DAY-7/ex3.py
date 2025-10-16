import datetime
import inspect
dtclassess = inspect.getmembers(datetime, inspect.isclass) 

# print('\nAll functions in datetime module:')
# for n, func in dtclassess:
#     # print(n,end="\t\n")
#     print("●",n)

# print('\n ---TODAY---\n')
# print(datetime.date.today())

# print('\n ---CURRENT DATE TIME---\n')
# print(datetime.datetime.now())

# print('\n ---CURRENT TIME---\n')
# print(datetime.datetime.now().time())

# print()

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I:%M:%S:%p')

print('\nCurrent time:\t\t', cttime)
print('Formated time: \t\t', formatedtime)
print()
