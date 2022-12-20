# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 10.01] => 0.19

myFile = open('data3.txt','r')
myList =list(map(float, myFile.readline().split()))

print(myList)

for i in range(len(myList)):
    myList[i] = abs(myList[i] - int(myList[i]))
print(round((max(myList) - min(myList)), 2))
