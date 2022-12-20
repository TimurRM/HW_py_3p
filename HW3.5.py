
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def checkInputNum():
    while True:
        try:
            num = int(input(f'Enter number, please: '))
            break
        except:
            print('This is not a number!!! Please, enter digits only!')
    return num

number = checkInputNum()

fiboList=[]

def fib(num):
     if num == 0:
         return 0
     elif num ==1:
         return 1
     elif num ==-1:
         return 1
     elif num < -1:
         return fib (num+2) - fib (num+1)
     else:
         return fib (num-1) + fib (num-2)

for i in range(- number, number + 1):
    fiboList.append(fib(i))

print(fiboList)