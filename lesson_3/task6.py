# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
x = [1, 2, -3,  -25, 0, 91, 100]
indMin = x.index(min(x))
indMax = x.index(max(x))
if indMin == indMax:
    y = []
elif indMin > indMax:
    y = x[indMax - 1 : indMin - 1]
else:
    y = x[indMin-1 : indMax - 1]

print(sum(y))
