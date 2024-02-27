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