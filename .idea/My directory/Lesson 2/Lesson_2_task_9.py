# var_1 = 37
# var_2 = 99
#Напишите код, который меняет значение переменных местами (var_1 должен быть равен 99 и var_2 — 37).

# Немного доработал, можно любые целые числа вводить

var1 = int(input("Введите первую переменную: "))
var2 = int(input("Введите вторую переменную: "))
a = var1
b = var2
a=a+b
b=a-b
a=a-b
print("Первая переменная теперь: ", a, "Вторая переменная теперь: ", b, "Переменные поменены местами")