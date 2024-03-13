#creating a class named Person

class Person:

    #creating a constructor to initialize parameters
    def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender

   #creating an introduction function     
    def Introduce(self):
              print ('hello '+self.name+' you are '+self.age+' years old and '+self.gender)


#creating an instance of Person
person1 = Person('brian','24','male')
#calling the introduce function
person1.Introduce()
