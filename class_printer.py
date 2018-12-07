class Printer:
    value = []
    
    def __init__(self, *value):
        self.value = value
        return
        
    def log(self):
        for value in self.value:
             print (value)
             
class FormattedPrinter(Printer):
     def log(self):
        for value in self.value:
             print ('***', value, '*****')
        
a = Printer('aaaaa', 'bbbbb','cccccc','ddddddd')
a.log()
b = FormattedPrinter('111111', 'ffffff','gdfgasdgasdf')
b.log()
    



