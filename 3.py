import time
from random import randint
import math
import numpy as np

def binSearch(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def fibSearch(arr, key):
    if len(arr) == 0: return -1

    fibM2 = 0
    fibM1 = 1
    fibM = fibM2 + fibM1

    while fibM < len(arr):
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1

    offset = -1

    while fibM > 1:

        i = min(offset + fibM2, len(arr) - 1)
        if arr[i] < key:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
        elif arr[i] > key:
            fibM = fibM2
            fibM1 -= fibM2
            fibM2 = fibM - fibM1
        else:
            return i

    if fibM1 and arr[len(arr) - 1] == key:
        return len(arr) - 1
    return -1

def interpolationSearch(arr, key):
    left = 0
    right = len(arr) - 1

    if right > -1:

        while arr[left] < key and arr[right] > key:
            if arr[right] == arr[left]:
                break
            mid = left + ((key - arr[left]) * (right - left)) // (arr[right] - arr[left])
            if arr[left] < key:
                left = mid + 1
            elif arr[mid] > key:
                right = mid - 1
            else: return mid

        if arr[left] == key: return left
        if arr[right] == key: return right

    return -1

def binnSearch(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key: return mid;
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def exponentSearch(arr, key):
    if arr[0] == key: return 0
    i = 1;
    while i < len(arr) and arr[i] <= key: i *= 2

    return binnSearch(arr, i//2, min(i, len(arr) - 1), key)


y_time_bin = []
y_time_fib = []
y_time_inter = []
y_time_exponent = []
x_col_vo_bin = []
x_col_vo_fib = []
x_col_vo_inter = []
x_col_vo_exponent = []

repetitions = 10

for i in range(1000, 100001, 1000):
    arr = sorted([randint(1, 100000) for _ in range(i)])
    key = arr[randint(0, i - 1)]

    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        binSearch(arr, key)
        finish_time = time.perf_counter()
        total_time += finish_time - start_time
    y_time_bin.append(total_time / repetitions)
    x_col_vo_bin.append(i)

    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        fibSearch(arr, key)
        finish_time = time.perf_counter()
        total_time += finish_time - start_time
    y_time_fib.append(total_time / repetitions)
    x_col_vo_fib.append(i)

    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        interpolationSearch(arr, key)
        finish_time = time.perf_counter()
        total_time += finish_time - start_time
    y_time_inter.append(total_time / repetitions)
    x_col_vo_inter.append(i)

    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        exponentSearch(arr, key)
        finish_time = time.perf_counter()
        total_time += finish_time - start_time
    y_time_exponent.append(total_time / repetitions)
    x_col_vo_exponent.append(i)


def plot_regression(x_data, y_data, label, color):
    coeffs = np.polyfit(np.log(x_data), y_data, 1)
    a, b = coeffs
    log_func = lambda x: a * np.log(x) + b
    print(f"Уравнение регрессионной кривой (логарифмическая) {label} — y = {a:.6f} * log(x) + {b:.6f}")
    x_fit = np.linspace(min(x_data), max(x_data), 100)
    y_fit = log_func(x_fit)
    plt.plot(x_fit, y_fit, label=label, color=color)


plt.figure(figsize=(10, 6))
plt.scatter(x_col_vo_bin, y_time_bin, label='Бинарный поиск')
plt.scatter(x_col_vo_fib, y_time_fib, label='Поиск Фибоначчи')
plt.scatter(x_col_vo_inter, y_time_inter, label='Интерполяционный поиск')
plt.scatter(x_col_vo_exponent, y_time_exponent, label='Экспоненциальный поиск')

plot_regression(x_col_vo_bin, y_time_bin, 'Бинарный поиск', 'red')
plot_regression(x_col_vo_fib, y_time_fib, 'Поиск Фибоначчи', 'green')
plot_regression(x_col_vo_inter, y_time_inter, 'Интерполяционный поиск', 'blue')
plot_regression(x_col_vo_exponent, y_time_exponent, 'Экспоненциальный поиск', 'grey')


plt.xlabel('n — количество элементов')
plt.ylabel('t — время работы алгоритма')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()