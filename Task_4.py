"""
Розділ 4
Описати функцію Arctg1 (x, ε) дійсного типу (параметри x, ε - дійсні, | x | <1, ε>0),
знаходить наближене значення функції arctg (x):
arctg (x) = x - x3/ 3 + x5/ 5 - ... + (-1) n· x2 · n + 1 / (2 · n + 1) + ....
В сумі враховувати всі складові, модуль яких більше ε. За допомогою Arctg1
знайти наближене значення arctg (x) для даного x при шести даних ε.
Скорий Євген 141
"""

def Arctg1(x, e):
    temp = x
    k = 1
    s = x
    while abs(temp) > e:
        temp = temp * x * x
        temp = temp * k
        k = k + 2
        temp = temp / k
        temp = -temp
        s += temp
        return s


x = float(input("Введіть X = "))

for i in range(6):
    e = float(input("Введіть є = "))
    print("arctg(x)", Arctg1(x, e))
