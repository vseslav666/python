COORD_Y = 'abcdefghij'


class Field:
    def __init__(self):
        field = ''
        self.field = field

    def create_field(self, empty_mark):
        self.empty_mark = empty_mark
        self.field = self.field.join([empty_mark for i in range(0, 100)])

    def change_field(self, coord, simbol):
        self.field = self.field[:coord - 1] + simbol + self.field[coord:]
        
    def print_field(self):
        print('  12345678910')
        j = 0
        for i in range(0, 100, 10):
            print(COORD_Y[j], self.field[i:i + 10])
            j = j+1

        
        
class Ship:
    def __init__(self, size):
        self.size = size
        self.ship_shape = 'None'
    def create_ship(self, empty_user_field):
        user_field = empty_user_field.field
        print (user_field[2])
        ship_coord = []
        last_input_coord = 0
        while len(ship_coord) != self.size:
            next_coord_ship = input(('Введите координты ' + str(self.size) + 'х палубного коробаля через запятую в виде a,1 \n'))
            y = next_coord_ship[0]
            x = next_coord_ship[2]
            curent_input_coord = (COORD_Y.index(y)*10 + int(x))
            print(last_input_coord - curent_input_coord)
            if empty_user_field.field[curent_input_coord - 1] == '~':
                empty_user_field.change_field(curent_input_coord, '*')
                ship_coord.append(curent_input_coord)
                empty_user_field.print_field()
                last_input_coord = curent_input_coord
            else:
                print('Выбранная координата уже занята')

empty_user_field = Field()
empty_user_field.create_field('~')

linkor = Ship(4)
linkor.create_ship(empty_user_field)

#kreyser1 = Ship(3)
#kreyser1.create_ship()
#kreyser2 = Ship(3)
#kreyser2.create_ship()


