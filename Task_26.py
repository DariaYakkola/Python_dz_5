# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
def degree(number1, number2, result=1) -> int:
    """Возводит первое число в степень второго числа"""
    if number2 == 0:
        return result
    else:
        result *= number1
        return degree(number1, number2 - 1, result)


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
print(f"Число {a} в степени {b} - {degree(a, b)}")
