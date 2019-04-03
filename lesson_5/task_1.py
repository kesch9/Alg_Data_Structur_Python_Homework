# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.
#
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
import collections
count = int(input("Введите количество предприятий: "))
Enteprise = collections.namedtuple('Enterprise',['quarter_1','quarter_2','quarter_3','quarter_4'])
dictEnteprise = collections.OrderedDict()
for i in range(1, count + 1):
    print()
    name =input("Введите данные название предприятия для " + str(i) + ": ")
    q1 = int(input("Введите прибыль за первый квартал: "))
    q2 = int(input("Введите прибыль за второй квартал: "))
    q3 = int(input("Введите прибыль за третий квартал: "))
    q4 = int(input("Введите прибыль за четвертый квартал: "))
    e = Enteprise(q1, q2, q3, q4)
    dictEnteprise[name] = e
averageCount = 0
averageDict = {}
for key, value in dictEnteprise.items():
    averageDict[key] = sum(value)/len(value)
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




