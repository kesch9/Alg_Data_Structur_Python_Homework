# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
a = ord(input("Введите первую букву "))
b = ord(input("Введите первую букву "))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'Место первой буквы = {a}, второй = {b}')
print(f'Разница = {abs(a-b)-1}')