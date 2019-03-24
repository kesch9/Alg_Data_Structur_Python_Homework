# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

print("Случайное целое число")
start = int (input())
end = int (input())
res = random.randint(start,end)
print(res)
print("Случайное вещественное число")
start = float (input())
end = float (input())
res = random.uniform(start,end)
print(res)
print("Случайный символ")
start = ord(input())
end = ord(input())
res = random.randint(start,end)
print(chr(res))