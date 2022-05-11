"""
Розділ 5
Описати функцію Count2(x) – кількість різних простих дільників числа х. Скласти
програму пошуку тих чисел в наборі з 6 чисел, що мають k різних простих дільників.
Скорий Євген 141
"""


def delitel(x):
    res = []
    i = 2
    while i * i < x + 1:
        if x % i == 0:
            res.append(i)
            while x % i == 0:
                x //= i
        i += 1
    if x != 1:
        res.append(x)

    print("Прості дільники - ", res)

    list = []
    print("Введіть 6 чисел")
    for i in range(6):
        list.append(int(input(": ")))

    result = []
    for i in res:
        if i in result:
            continue
        for j in list:
            if i == j:
                result.append(i)
                break

    return "З 6 чисел та чисел дільника співпалають такі - " + str(result)


a = int(input("Введіть число = "))

print(delitel(a))

