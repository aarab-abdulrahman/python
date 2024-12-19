from datetime import date

class Person : 
    numbre_person=0

    def __init__ (self,idx,age="none",nom="none",prenom="none"):
        self.__idx=id(self) # "__"  --> encapsulation
        self.__agee=age
        self.__nom=nom
        self.__prenom=prenom

        Person.numbre_person+=1

    def __str__(self):
        return f"""
            id : {self.__idx}
            nom : {self.__nom}
            prenom : {self.__prenom}
            age : {self.__agee}
        """
    
    def number_of_person(self):
        return f"number of person is : {Person.numbre_person} and my age is {self.__agee}"
    
    @staticmethod
    def from_birthday_year(Pers,idx,birth_day_year,nom,prenom):
            return Pers(idx,date.today().year-birth_day_year,nom,prenom)
    
    




ayoub=Person("1","21","ayoub","mokrich")

abdulrahman=Person("2","18","abdulrahman","aarab")

mohamed=Person("3","22",'mohamed',"xx")


# print(Person.number_of_person())

# print(ayoub.age)
# print(ayoub.__str__()) 
# print(Person.number_of_person())

# print(ayoub , abdulrahman , mohamed)

new=Person.from_birthday_year(Person,"1",2000,'ayoub','mokrich')
print(ayoub.__str__())
print(new)


class Couscouse:
     def __init__ (self,ingredients):
          self.ingredients=ingredients
     @classmethod
     def moroccan(item):
          return item(['Carrots','tomatoes'])
     def prazil(item):
          return item(['Pepper'])

item1=Couscouse(['nothing'])
item2=Couscouse.moroccan()

print(item1,item2)

    
