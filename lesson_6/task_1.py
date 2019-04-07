# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
import time

from memory_profiler import profile
import collections
import random
@profile
def my_func():
    count = int(input("Введите количество предприятий: "))
    Enteprise = collections.namedtuple('Enterprise', ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
    dictEnteprise = collections.OrderedDict()
    for i in range(1, count + 1):
        print()
        name = input("Введите данные название предприятия для " + str(i) + ": ")
        q1 = int(input("Введите прибыль за первый квартал: "))
        q2 = int(input("Введите прибыль за второй квартал: "))
        q3 = int(input("Введите прибыль за третий квартал: "))
        q4 = int(input("Введите прибыль за четвертый квартал: "))
        e = Enteprise(q1, q2, q3, q4)
        dictEnteprise[name] = e
    averageCount = 0
    averageDict = {}
    for key, value in dictEnteprise.items():
        averageDict[key] = sum(value) / len(value)
        averageCount += averageDict[key]
    print()
    print("Средняя прибыль всех предприятий = " + str(averageCount))
    print()
    print("Предприятия с прибылью выше среднего: ")
    for key, value in averageDict.items():
        a = sum(dictEnteprise[key])
        if a > averageCount:
            print("Компания " + key + " заработала " + str(a))

    print()
    print("Предприятия с прибылью ниже среднего: ")
    for key, value in averageDict.items():
        a = sum(dictEnteprise[key])
        if a < averageCount:
            print("Компания " + key + " заработала " + str(a))
    a = [averageDict] * (10 ** 6)
    b = [dictEnteprise] * (10 ** 6)
    c = [Enteprise] * (10 ** 6)
@profile
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


@profile
# вариант 2
def two_min_2():
    SIZE = 1000
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)

if __name__ == '__main__':
   two_min_1()
   time.sleep(4)
   two_min_2()
