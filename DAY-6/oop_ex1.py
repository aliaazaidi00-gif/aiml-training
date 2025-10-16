# class Player:
#     def __init__(self):
#         print('Welcome to Player Class')

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f'Id:{self.id} \t Name:{self.name} \t team: {self.team}')

# #object creation
# p1=Player()
# p2=Player()
# p3=Player()
# p1.reg(1,'Syahmi','Malaysia')
# p2.reg(2,'Alia','Brazil')
# p3.reg(3,'Nurul','England')

# p1.display()
# p2.display()
# p3.display()
# print()

#PARAMETER CONSTRUCTOR
class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id:{self.id} \t Name:{self.name} \t team: {self.team}')

    def __str__(self):
        return (f'\n{self.id},{self.name},{self.team}')

#object creation
p1=Player(1,'Syahmi','Malaysia')
p2=Player(2,'Alia','Brazil')
p3=Player(3,'Nurul','England')

# displaying first player details
p1.display()
p2.display()
p3.display()

print(p1)
print(p2)
print(p3)