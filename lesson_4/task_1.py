# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
import random
import timeit

# вариант 1
def two_min_1():
    SIZE = 1000
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_first, min_second = (0, 1) if array[0] > array[1] else (1, 0)
    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam
        elif array[i] < array[min_second]:
            min_second = i


# вариант 2
def two_min_2():
    SIZE = 1000
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)

print(timeit.timeit("two_min_1()", setup="from __main__ import two_min_1", number = 1000))
print(timeit.timeit("two_min_2()", setup="from __main__ import two_min_2", number = 1000))
