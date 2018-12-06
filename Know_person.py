class Person:
    name = ''
    age = None
    list_know_person = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def know(self, person):
        self.person = person
        self.list_know_person[person.name]  = person.age
        return
    def is_known (self, person):
        self.person = person
        if person.name in self.list_know_person:
            print(self.name, 'знает', person.name )
        else:
            print(self.name, 'не знает', person.name )
            
      
                
            
Andrey = Person('Andrey', 22)
Leha = Person('Alexey', 12)
Diman = Person('Dmitry', 46)
Olya = Person('Olga', 16)
Andrey.know(Leha)
Andrey.know(Diman)
Andrey.is_known(Diman)
Andrey.is_known(Olya)
 