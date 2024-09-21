import random


def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 7

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У вас есть 7 попыток, чтобы его угадать.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}. Введите ваше предположение: "))

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
                break
        except ValueError:
            print("Ошибка: введите целое число.")
    else:
        print(f"К сожалению, вы не угадали. Загаданное число было {secret_number}.")


guess_the_number()
