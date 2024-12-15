from random import  randint
import math

def min_val(arr):
    if len(arr) == 0: return None
    value = arr[0]
    for i in range(len(arr)):
        if arr[i] < value: value = arr[i]
    return value

def max_val(arr):
    if len(arr) == 0: return None
    value = arr[0]
    for i in range(len(arr)):
        if arr[i] > value: value = arr[i]
    return value

def min_max(arr):

    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0], arr[0]
    else:
        if len(arr) % 2 != 0:
            min_v = max_v = arr[0]
            i = 1
        else:
            if arr[0] > arr[1]:
                min_v = arr[1]
                max_v = arr[0]
            else:
                min_v = arr[0]
                max_v = arr[1]
            i = 2

        while i < len(arr):
            if arr[i] > arr[i + 1]:
                if arr[i + 1] < min_v: min_v = arr[i + 1]
                if arr[i] > max_v: max_v = arr[i]
            else:
                if arr[i] < min_v: min_v = arr[i]
                if arr[i + 1] > max_v: max_v = arr[i + 1]
            i += 2

    return min_v, max_v

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

def binSearch(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key: return mid;
        if arr[mid] < key:
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

def exponentSearch(arr, key):
    if arr[0] == key: return 0
    i = 1;
    while i < len(arr) and arr[i] <= key: i *= 2

    return binSearch(arr, i//2, min(i, len(arr) - 1), key)

arr = [randint(1, 20000) for i in range(10)]
#arr = [1, 2, 3, 4, 5, 6]
key = arr[9]
print(arr)
print(key)
print(linearSearch(arr, key))