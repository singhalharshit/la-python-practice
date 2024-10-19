# Class - Classification/Segmentation or Blueprint of a real time entity
# Objests - The real time entity

class Person:
    def __init__(self,name,surname,email_id, yob):   # __init__ is nothing but initialization of any variable to the classes, and SELF is a pointer which will direct anything to the class
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = yob


    def age_calc(self,crrntyr):
        return crrntyr- self.year_of_birth

    
s= Person('Harshit', 'Singhal', 'abc@gmail.com', 2000)
print(s.name)
print(s.surname)
print(s.email_id)
print(s.year_of_birth)
print(s.age_calc(2024))
