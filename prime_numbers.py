#Простые числа
#Программа высчитывает все простые числа от нуля до указанного пользователем
print('введите число')
a = int(input())
answer = []#Список простых чисел

for i in range(2, a):
    prime = True
    for j in range(2, i):
       if (i%j == 0):     
           prime = False
    if prime:
       answer.append(i)
            

            
print(answer)
            
