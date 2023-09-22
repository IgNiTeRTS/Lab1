import math

a = float(input('Введите корень а = '))
b = float(input('Введите корень b = '))
c = float(input('Введите корень c = '))

ds = b ** 2 - 4 * a * c
if ds < 0:
    print('Вычисление невозможно, т.к. дискриминант меньше нуля')

if ds > 0:
    x1 = (-b + math.sqrt(ds)) / (2 * a)
    x2 = (-b - math.sqrt(ds)) / (2 * a)
    print('Два корня уравнения', x1, x2)
elif ds == 0:
    x1 = (-b / (2 * a))
    print('Один корень уравнения', x1)
