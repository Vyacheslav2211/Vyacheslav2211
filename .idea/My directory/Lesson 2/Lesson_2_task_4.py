# Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# Функция должна печатать числа от 1 до n. При этом:
#   1. если число делится на 3, печатать `Fizz`;
#  2. если число делится на 5, печатать `Buzz`;
# 3. если число делится на 3 и на 5, печатать `FizzBuzz`
list = []
n=int(input("Введите число: "))
n=n + 1
for i in range(1,n):
    if i%15 == 0:
        list.append('FizzBuzz')
    elif i%3 == 0:
        list.append('Fizz')
    elif i%5 == 0:
        list.append('Buzz')
    else:
        list.append(i)
print(list)