def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else: 
        return False

year = int(input("Введите год: "))

if is_leap_year(year):
    print(year, "Это високосный год")
else :
    print(year, "Это не високосный год")

            