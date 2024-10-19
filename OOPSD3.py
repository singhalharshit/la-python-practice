# Public Private and Protected Concepts

class Person():
    _name = 'Sid'
    __surname = 'Kumar'
    yob = 2000

    def _age (self, current_year):
        return current_year - self.yob
    
    def __age (self, current_year):
        return current_year - self.yob


person_obj = Person()
print(person_obj.yob)
print(person_obj._name)
print(person_obj._age(2024))
print(person_obj._Person__age(2025))

print('------------------------------------------------------')
print('######################################################')
print('------------------------------------------------------')

class Employee(Person):
    _name = 'Sudh'
    __surnmame = 'Krish'
    yob = 2001


emp_obj = Employee()

print(emp_obj.yob)
print(emp_obj._name)
print(emp_obj._age(2024))
print(emp_obj._Person__age(2025))





