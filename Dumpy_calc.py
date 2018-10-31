#Примитивный калькулятор
print('Введите первое число')
a = input()
print('Введите второе число')
b = input()
print('Введите + или -')
c = input()

if c == ('+'):
    print (int(a) + int(b))
elif c == ('-'):
    print (int(a) - int(b))
else:
    print('Введен неверный знак математической операции')
    
    
    