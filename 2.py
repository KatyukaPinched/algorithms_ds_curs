import time
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

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

def jumpSearch(arr, key):
    step = i = 0

    while arr[min(step, len(arr) - 1)] < key:
        i = step
        step += int(math.sqrt(len(arr)))
        if i >= len(arr):
            return -1
    while arr[i] <= key:
        if arr[i] == key:
            return i
        elif i == min(step, len(arr)):
            return -1
        i += 1
    return -1


y_time_lin = []
y_time_bin = []
y_time_jump = []
x_col_vo_lin = []
x_col_vo_bin = []
x_col_vo_jump = []

repetitions = 10

for i in range(1000, 100001, 1000):
    arr = sorted([random.randint(1, 100000) for _ in range(i)])
    key = arr[random.randint(0, i - 1)]

    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        linearSearch(arr, key)
        finish_time = time.perf_counter()
        total_time += finish_time - start_time
    y_time_lin.append(total_time / repetitions)
    x_col_vo_lin.append(i)

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
        jumpSearch(arr, key)
        finish_time = time.perf_counter()
        total_time += finish_time - start_time
    y_time_jump.append(total_time / repetitions)
    x_col_vo_jump.append(i)


p_lin = np.polyfit(x_col_vo_lin, y_time_lin, 1)
polinom_lin = np.poly1d(p_lin) # Исправлено: p_lin вместо p
print("Уравнение регрессионной кривой для линейного поиска — ", polinom_lin)

coeffs = np.polyfit(np.log(x_col_vo_bin), y_time_bin, 1)
a, b = coeffs
log_func = lambda x: a * np.log(x) + b
print("Уравнение регрессионной кривой (логарифмическая) для бинарного поиска — ", f"y = {a:.6f} * log(x) + {b:.6f}")

def sqrt_func(x, a, b):
    return a * np.sqrt(x) + b

params, covariance = curve_fit(sqrt_func, x_col_vo_jump, y_time_jump)
a, b = params
print(f"Уравнение регрессионной кривой (квадратный корень) для поиска прыжками: y = {a:.6f} * sqrt(x) + {b:.6f}")


plt.figure(figsize=(10, 6))
plt.scatter(x_col_vo_lin, y_time_lin, label='Линейный поиск')
plt.scatter(x_col_vo_bin, y_time_bin, label='Бинарный поиск')
plt.scatter(x_col_vo_jump, y_time_jump, label='Поиск прыжками')

plt.plot(x_col_vo_lin, polinom_lin(x_col_vo_lin), label='Линейный поиск (регрессия)', color='red')
plt.plot(x_col_vo_bin, log_func(x_col_vo_bin), label='Бинарный поиск (регрессия)', color='green')
plt.plot(x_col_vo_jump, sqrt_func(x_col_vo_jump, *params), label='Поиск прыжками (регрессия)', color='blue')


plt.xlabel('n — количество элементов')
plt.ylabel('t — время работы алгоритма')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
