while True:
   try:
      my_age = float(input("Введите число:")) # считывание вводимых символов и преобразование в число
      break # если успешно, то выход из цикла
   except ValueError:
      print("Вводите только числа") # если не удалось преобразовать в число, выводится сообщение и цикл повторяется

print("Ваш возраст: ", my_age , "лет")

my_age = my_age + 1

print("Ваш возраст через год : ", my_age , "лет")