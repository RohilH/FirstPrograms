class Person:
	def __init__(self, age, name):
		self.age = age
		self.name = name

Ro = Person(18, "Rohil")
A = Person(51, "Atul")
Ru = Person(14, "Runali")
V = Person(44, "Viveka")

def compPers(Person1, Person2):
        if((Person1.age == Person2.age) & (Person1.name == Person2.name)):
                print("These two people are the same!")
        if(Person1.age < Person2.age):
                print(Person2.name, "is older than", Person1.name, "by", Person2.age - Person1.age, "years")
        else:
                print(Person1.name, "is older than", Person2.name, "by", Person1.age - Person2.age, "years")

compPers(Ro,A)
compPers(Ru,Ro)
compPers(V,A)
compPers(V,Ru)



