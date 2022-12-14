# Завдання 3
# Напишіть програму, яка розв'язує квадратне рівняння 𝑎𝑥 2 + 𝑏𝑥 + 𝑐 = 0 у дійсних числах.
# На відміну від аналогічної вправи з минулого уроку, програма повинна видавати повідомлення
# про відсутність дійсних коренів, якщо значення дискримінанта 𝐷 = 𝑏 2 −4𝑎𝑐 негативне, єдине
# рішення 𝑥 = − 𝑏 / 2𝑎 , якщо він дорівнює нулю, або два корені 𝑥1,2 = −𝑏±𝐷‾‾√/2𝑎, якщо він
# позитивний.

import math

a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Коренів не має')
