# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


myFile = open('data2.txt','r')
myList =list(map(int, myFile.readline().split()))

print(myList)

multyList = []
if len(myList) % 2 == 0:
     size = len(myList) // 2
else:
    size = (len(myList) // 2) + 1

for i in range(size):
    multyList.append(myList[i] * myList[-(i + 1)])
print(multyList)
