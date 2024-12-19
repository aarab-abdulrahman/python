class Person : 
    numbre_person=0

    def __init__ (self,idx,age="none",nom="none",prenom="none"):
        self.idx=id(self) 
        self.age=age
        self.nom=nom
        self.perenom=prenom

        Person.numbre_person+=1

    def __str__(self):
        return f"""
            id : {self.idx}
            nom : {self.nom}
            prenom : {self.perenom}
            age : {self.age}
        """

    @staticmethod
    def number_of_person():
        return f"number of person is : {Person.numbre_person}"




m9rach=Person("1","21","mouad","mokrich")

abdulrahman=Person("2","18","abdulrahman","aarab")

mohamed=Person("3","22",'mohamed',"xx")


print(m9rach , abdulrahman , mohamed)

print(Person.number_of_person())