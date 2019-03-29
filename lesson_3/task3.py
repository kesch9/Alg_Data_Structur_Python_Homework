# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import sys

def changeMaxMin(x):
    max = 0
    indexMax = 0
    min = sys.maxsize
    indexMin = 0
    if (type(x) == list):
        index = 0
        for i in x:
            if max < i:
                max = i
                indexMax = index
            if min > i:
                min = i
                indexMin = index
            index += 1
        x[indexMax] = min
        x[indexMin] = max
    return x

arr = [1,2,4,5,6,2,1]
print(changeMaxMin(arr))
print(changeMaxMin('2342'))