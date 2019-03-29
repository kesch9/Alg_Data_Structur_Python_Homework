# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
x = list(range(2,100))
y = list(range(2,9))
print()
rez =[]
for i in x:
    ind = 0
    for j in y:
        if i%j == 0:
            ind += 1
    rez.append(ind)
print(rez)