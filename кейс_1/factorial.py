import math

def calculate_factorial():
    try:
        number = int(input("Введите число: "))

        if number < 0:
            raise ValueError("Число должно быть положительным.")

        result = math.factorial(number)

        print(f"Факториал числа {number} равен {result}.")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


calculate_factorial()
