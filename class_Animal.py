class Animal:
    name = ''
    feature = []
    animal = {}
    def __init__ (self, name, *feature):
        self.name = name
        self.feature = feature
        self.animal = {name : feature}
#        print(self.animal)
        return

        
class Human():
    def is_dangerous (animal, name):
        dangerouse_feature = ['predator', 'poison']
        c = str(animal.values())
        dangerous_flag = ('None')
        for i in dangerouse_feature:
            if i in c:
                dangerous_flag = ('True')
                break
        if dangerous_flag == 'True':
            print (name, ' is dangerous')
        else:
            print(name, 'is no dangerous')
        
                
               
                     

                
            

animal1 = Animal('Lion','cat', 'predator')
animal2 = Animal('Rattlesnake', 'snake', 'poison')
animal3 = Animal('Cow', 'herbivorous')


Human.is_dangerous(animal1.animal, animal1.name)