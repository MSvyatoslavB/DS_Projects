"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # количество попыток
    initial = 1  # начальное число
    finite = 100  # конечное число
    average = initial + (finite - initial) // 2  # среднее число

    while True:
        count += 1
        if number == average:
            break  # выход из цикла если угадали
        elif number > average:
            initial = average + 1  # сдвигаем нижнюю границу на одно число после среднего
        else:
            finite = average - 1  # сдвигаем верхнюю границу на одно число перед средним
        average = (initial + finite) // 2
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
