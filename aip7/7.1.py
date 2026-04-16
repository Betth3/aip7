list=[1,37,56,78,99]
number = int(input("Введите любое число: "))
if number in list:
    print("Поздравляю, Вы угадали число!")
    print("Исходный список: ", list)
    print(f"Ваше число: {number}")
else:
    print("Нет такого числа!")
    print("Исходный список: ", list)
    print(f"Ваше число: {number}")
