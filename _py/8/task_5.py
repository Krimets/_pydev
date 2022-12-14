# Завдання 5
# Створіть програму, яка приймає як формальні параметри зріст і вагу користувача, обчислює індекс маси тіла і в
# залежності від результату повертає інформаційне повідомлення (маса тіла в нормі, недостатня вага або слідкуйте
# за фігурою). Користувач з клавіатури вводить значення росту та маси тіла та передає ці дані у вигляді фактичних
# параметрів під час виклику функції. Програма працює доти, доки користувач не зупинить її комбінацією символів «off».


def bmi_function(a, b):
    bmi = a / (b * b)
    if 18.4 < bmi < 25.1:
        return f"Маса тіла в нормі, індекс маси тіла = {bmi}"
    elif bmi > 25:
        return f"Слідкуйте за фігурою, індекс маси тіла = {bmi}"
    else:
        return f"Недостатня вага, індекс маси тіла = {bmi}"


def request():
    r = input('''
Обчислити індекс маси тіла = Натисніть 1
Для виходу = off
>>> ''')
    if r == 'off':
        print('Завершення програми')
    elif r == '1':
        print(bmi_function(float(input('''Введіть масу
>>> ''')), float(input('''Введіть зріст в метрах (Наприклад 1.78)
>>> '''))))
        request()
    else:
        print('Спробуйте ще раз')
        request()


request()
