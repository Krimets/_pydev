# Завдання 5
#  Напишіть програму для перевірки введеного числа на ознаку парності. Якщо число
#  парне/непарне – вивести відповідне повідомлення на екран. Для опису цього алгоритму
#  використовувати тернарний оператор.

print('парне' if int(input('Введiть число: ')) % 2 == 0 else 'непарне')
