# class Account: 
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self, amount):
#         self.bal+=amount

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#              self.bal-=amount
#              print('balance after withdraw:',self.bal)
#         else:
#              print('Insufficient amount in account')
#              print('Transaction Failed!!')
#     def show(self):
#          print(f'\nAccount Holder Name: \t {self.ac_holder:<10} Account Balance: \t {self.bal:>3}')

# ac1=Account('Alia',50000)
# ac2=Account('Syahmi',78932)
# ac1.show()
# ac2.show()

# ac1=Account('Alia',50000)
# ac1.show()
# wamount=float(input('Enter amount to withdraw:'))
# ac1.withdraw(wamount)

# class Account:
#     def __init__(self,balance,ac_holder):
#         self.balance = balance
#         self.account = ac_holder
    
#     def get_balance(self):
#         return self.balance

# acc = Account(1000,'Alia')
# acc_balance=34000
# print(acc.balance)

class Account: 
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self, amount):
        self.bal+=amount

    def withdraw(self,amount):
        if(self.bal>=amount):
             self.bal-=amount
             print('Balance after withdrawn\t\t\t:',self.bal)
        else:
             print('Insufficient amount in account')
             print('Transaction Failed!!')
    def show(self):
         print(f'\nAccount Holder Name: \t {self.ac_holder} \nAccount Balance: \t {self.bal}')


ac=Account('Alia',23000)
ac.show()

while True:
    print('\nPlease choose:1.Deposit\t\t 2.Withdraw')
    choice=int(input('\nYour Number\t\t\t\t:'))
    if(choice==3):
        ac.show()
    else:
        if(choice==1):
            damount=float(input('Enter amount to deposit\t\t\t:'))
            ac.deposit(damount)
        if(choice==2):
            damount=float(input('Enter amount to withdraw\t\t:'))
            ac.withdraw(damount)
        if(choice==3):
            ac.show()
        else:
            print('Wrong Choice')