# Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
i = 0
a = 32
while i < 9:
    print("---------------------------------------------------")
    s = ""
    j = 0
    while j < 10:
        s += "|" + str(a)+ "-" + chr(a)
        j += 1
        a += 1
    s+="|"
    print(s)
    i += 1
print("--------------------------------------------------------")
s = ""
j = 0
while j < 6:
    s += "|" + str(a)+ "-" + chr(a)
    j += 1
    a += 1
s+="|"
print(s)
