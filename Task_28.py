# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.
def sum(number1, number2) -> int:
    """Возвращает сумму двух целых чисел"""
    if number1 > number2:
        if number2 == 0:
            return number1
        else:
            while number2 != 0:
                return sum(number1 + 1, number2 - 1)
    else:
        if number1 == 0:
            return number2
        else:
            while number1 != 0:
                return sum(number1 - 1, number2 + 1)


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
print(sum(a, b))
