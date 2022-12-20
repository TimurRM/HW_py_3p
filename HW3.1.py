# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной идексах.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

myFile = open('data.txt','r')
myList =list(map(int, myFile.readline().split()))

print(myList)

summ = 0
for i in range(len(myList)):
    if i % 2 != 0:
        print(f'+ {myList[i]}', end=' ')
        summ += myList[i]
print(f' =  {summ}')


