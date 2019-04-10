# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.
from memory_profiler import profile
import random
import timeit


def merge(left,right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
# @profile
def mergesort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)



testLst = [int(random.uniform(0, 100) * 100) / 100 for _ in range(30)]
print(testLst)
print(mergesort(testLst))
print(timeit.timeit("mergesort([75.94, 5.91, 34.14, 51.47, 72.45, 50.87, 75.9, 93.63, 80.43, 4.01, 14.03, 24.16, "
                    "95.31, 39.87, 31.05, 92.08, 50.88, 4.49, 32.67, 50.99, 63.33, "
                    "70.02, 38.64, 76.8, 93.71, 3.27, 63.21, 74.38, 60.77, 41.18])",
                    setup="from __main__ import mergesort", number = 1000))
# if __name__ == '__main__':
#    testLst = [int(random.uniform(0, 100) * 100) / 100 for _ in range(200)]
#    mergesort(testLst)
# python3 -m memory_profiler task2.py