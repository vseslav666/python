# Калькулятор подсетей

a = 16
i = 0
decimal_mask = ''
# Преобразование маски в двоичный формат
mask = ['0' for i in range(0, 32)]
while i < a:
    mask.remove('0')
    mask.insert(i, '1')
    i += 1
# Преобразование маски в десятичный формат
for i in range(0, 32, 8):
    bin_to_dec = mask[i:i+8]
    bin_to_dec = (''.join(bin_to_dec))
    decimal = int(bin_to_dec, 2)
    decimal_mask = (decimal_mask + str(decimal) + '.')
decimal_mask = decimal_mask[:-1]

for i in range(8, 40, 9):
    mask.insert(i, ' ')

binary_mask = (''.join(mask))
print('Битовое представление /',a)
print('Двоичное представление ', binary_mask)
print('Десятичное представление', decimal_mask)
