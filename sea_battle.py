COORD_Y = 'abcdefghij'

def print_field(field):
    print('  12345678910')
    j=0
    for i in range(0, 100, 10):
        print(COORD_Y[j],field[i:i + 10])
        j=j+1

user_field = ''
user_field = user_field.join(['~' for i in range (0, 100)])
    
ai_field = ''
ai_field = ai_field.join(['?' for i in range(0, 100)])
        
        
class Ship:
    def __init__(self, size):
        self.size = size
    
    def create_ship(self):
        global user_field
        ship_coord = []
        while len(ship_coord) != self.size:
            next_coord_ship = input(('Введите координты ' + str(self.size) + 'х палубного коробаля через запятую в виде a,1 \n'))
            y = next_coord_ship[0]
            x = next_coord_ship[2]
            last_input_coord = (COORD_Y.index(y)*10 + int(x))
            print(last_input_coord)
            if user_field[last_input_coord - 1] == '~':
                user_field = user_field[:last_input_coord - 1] + '*' + user_field[last_input_coord:]
                ship_coord.append(last_input_coord)
                print_field(user_field)
            else:
                print('Выбранная координата уже занята')


    
print_field(user_field)

linkor = Ship(4)
linkor.create_ship()

kreyser1 = Ship(3)
kreyser1.create_ship()

kreyser2 = Ship(3)
kreyser2.create_ship()


