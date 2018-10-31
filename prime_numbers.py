#Простые числа
#Программа высчитывает все простые числа от нуля до указанного пользователем
print('введите число')
a = 10
#a = int(input())
i = 2 #переменная для записи чисел в список
lst = []#Список для записи всех чело от 1 до заданного
answer = []#Список простых чисел
while i <= a:
    lst.append(i)
    i = i+1
#print(lst)
i = 1 
for i in range(2, a):
    i +=1
    j = 1
    while j <= i:
        if j % i == 0:
            j = j + 1
            break
        else:
            answer.append(j)
            j = j + 1
            
print(answer)
            
    