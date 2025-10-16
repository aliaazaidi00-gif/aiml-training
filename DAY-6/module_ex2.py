# import datetime
# import inspect

# print('Today is (Date):',datetime.date.today())

# dtclasses=inspect.getmembers(datetime, inspect.isclass)
# print('\nAll classes inside datetime module\n')

# for n, func in dtclasses:
#     print(n)

# print('\nAll functions inside datetime.date class\n')

# functions=inspect.getmembers(datetime.date, inspect.isbuiltin)
# for n,func in functions:
#     print(n)

import os
# import inspect
# functions=inspect.getmembers(os, inspect.isbuiltin)
# for n,func in functions:
#     print(n)

listdir=os.listdir()
for dir in listdir:
    print(dir)

# print(os.listdir())

