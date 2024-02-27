import math

def square(side_lenght):
    # функция вычисляет площадь квадрата 
    # и округляет вводимое число вверх, если оно не является целым числом
   rounded_side_lengt = math.ceil(side_lenght)# округление числа
   return rounded_side_lengt ** 2
side = float(input("Введите сторону квадрата: "))

print("Площадь квадрата со стороной", side, "равна", square(side))