# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random
import timeit
# from memory_profiler import profile
# @profile()
def bubbleSort (arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

testLst = [random.randint(-100, 100) for _ in range(10)]
print(testLst)
print(bubbleSort(testLst))

# Тестирование времени работы
print(timeit.timeit("bubbleSort([75.94, 5.91, 34.14, 51.47, 72.45, 50.87, 75.9, 93.63, 80.43, 4.01, 14.03, 24.16, "
                    "95.31, 39.87, 31.05, 92.08, 50.88, 4.49, 32.67, 50.99, 63.33, "
                    "70.02, 38.64, 76.8, 93.71, 3.27, 63.21, 74.38, 60.77, 41.18])",
                    setup="from __main__ import bubbleSort", number = 1000))

# Тестирование по памяти
# if __name__ == '__main__':
#    testLst = [random.randint(-100, 100) for _ in range(200)]
#    bubbleSort(testLst)
# python3 -m memory_profiler task1.py