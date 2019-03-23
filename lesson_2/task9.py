# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
max = 0
sum = 0
while True:
    print("Введите натуральное число или 0 чтоб выйти")
    a = str(input())
    if a == '0':
        break
    temp_sum = 0
    for i in a:
        temp_sum += int(i)
    if temp_sum > sum:
        sum = temp_sum
        max = int(a)
    print("Число = " + str(max) + " Сумма = " + str(sum))
