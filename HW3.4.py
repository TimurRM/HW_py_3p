# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def checkNum():
    while True:
        try:
            num = int(input(f'Enter number, please: '))
            break
        except:
            print('This is not a number!!! Please, enter digits only!')
    return num


decimalNum = checkNum()

binaryNum = ''
while decimalNum > 0:
    binaryNum = str(decimalNum % 2) + binaryNum
    decimalNum = decimalNum // 2
  
print(binaryNum)
