class Person:
    def __init__(self,name, surname,yob):
        self._name=name # Now in this case we have created a protected variable by using (_) which makes a public variable to protected variable. It is done inorder to restrict user from changing 
        self.__surname=surname # Now in this case we have made a variable private
        self.year_of_birth= yob


ojb1= Person('Harshit','Singhal','2000')
print(ojb1)

print(ojb1._name) 
print(ojb1._Person__surname) # Inorder to call a class variable we need to call it this way always _className__classVariable
