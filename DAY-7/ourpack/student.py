class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def print_info(self):
        print('\nStudent ID:',self.id)
        print('Student Name:',self.name)