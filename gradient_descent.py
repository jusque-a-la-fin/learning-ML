import numpy as np

# Фукция, для которой ищется глобальный минимум
def function(x, y):
    return x ** 4 + 2*x**2*y + 10*x**2 + 6*x*y + 10*y**2 - 6*x + 4

# Градиент функции
def gradient(x, y):
    # Производная по x
    df_dx = 4*x**3 + 4*x*y + 20*x + 6*y - 6

    # Производная по y
    df_dy = 2*x**2 + 6*x + 20*y

    # градиент функции
    df = np.array([df_dx, df_dy])
    return df

# Функция, реализующая градиентный спуск
def Perform_gradient_descent(numberOfIterations, eps, xy_start,
                       learning_rate, coefficient):

    # инициализация аргумента функции начальным значением
    xy = xy_start

    # изменение аргумента
    delta_xy = np.zeros(xy.shape)

    # шаг гр.спуска
    i = 0

    # разность последних значений функции
    difference = 1

    # список значений функции
    f_xy = []

    # добавление начального значения функции
    f_xy.append(function(xy[0], xy[1]))

    while  i < numberOfIterations and difference > eps:
        # ядро гр. спуска
        delta_xy = -learning_rate * gradient(xy[0], xy[1]) + coefficient*delta_xy
        xy = xy + delta_xy

        # добавление очередного знач. функции
        f_xy.append(function(xy[0], xy[1]))

        i += 1

        # разность последних значений функции
        difference = abs(f_xy[-1] - f_xy[-2])

    print(" Глобальный минимум в точке:\n x: {:.3f}"
          " y: {:.3f} f(x,y): {:.3f}".format(xy[0], xy[1], f_xy[-1]))

# главная функция
def main():
    # число итераций градиентного спуска
    numberOfIterations = 10000

    # точность
    eps = 0.001

    # определяет размер шага на каждой итерации
    # при движении к глобальному минимуму
    learning_rate = 0.1

    # коэффициент, исправляющий недостатки гр.спуска
    coefficient = 0.6

    # помогает генерировать одни и те же случайные числа
    rand = np.random.RandomState(18)

    # инициализация аргумента функции начальным значением
    xy_start = rand.uniform(-2, 2, 2)

    # Запустить градиентный спуск
    Perform_gradient_descent(numberOfIterations, eps, xy_start, learning_rate, coefficient)

# вызов главной функции
main()
