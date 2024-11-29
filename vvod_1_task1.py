# Практическое задание по уроку "Базовые структуры данных"
#
# Цель: применить и закрепить базовые знания о структурах данных, решив набор задач.
#
# Формат решения:
# Можете написать код всех задач в одном файле main.py.
# Можете написать код в разных файлах к каждой задаче: task1.py, task2.py и т.д.
#
# Задачи.
# Предисловие:
# Если в задаче говориться о том, что нужно вывести результат арифметических действий, сравнения и других операций, то вам нужно сначала составить выражение с исходными данными, а не вывести результат этого выражения сразу.
# Пример: сложите числа 12 и 89, вычтите число1 и выведите результат на экран,
# Верно: print(12 + 89 - 1)
# Не верно: print(100)
#
# Задача 1 (просто) "Арифметика":
# Напишите в начале программы однострочный комментарий: "1st program".
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
# Предполагаемый результат: 15.0

#"1st program"
print(9 ** 0.5 * 5)
print('************************')


# Задача 2 (просто) "Логика":
# Напишите в начале программы однострочный комментарий: "2nd program".
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
#  Предполагаемый результат: True

#"2nd program"
print(9.99 >= 9.98 and 1000 != 1000.1)
print('************************')

# Задача 3 (средне) "Школьная загадка":
# Напишите в начале программы однострочный комментарий: "3rd program".
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
# Выведите на экран(в консоль) результат сравнения этих двух выражений.
# Предполагаемый результат (с использованием ==): False


#"3rd program"
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2) == (2 * (2 + 2)))
print('************************')

# Задача 4 (сложно) "Первый после точки":
# Напишите в начале программы однострочный комментарий: "4th program".
# Дана строка '123.456'.
# Вывести на экран первую цифру после запятой - 4.
# Начало алгоритма решения:
# Преобразуйте в строку в дробное число. ('123.456' -> 123.456)
# Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)
# Следующие шаги алгоритма составьте самостоятельно. В них вам понадобится команда int() и остаточное деление на 10.

#"4th program"
# По этапно
# a = '123.456'
# a1 = float('123.456')
# print(a1)
# b = int(a1 * 10)
# print(b)
# c = b % 10
# print(c)

# свернутый код
print((int((float('123.456') * 10))) % 10)
print('************************')

# Примечания:
# Старайтесь не торопиться и делать перерывы, если зашли в тупик при решении.
# Выполняйте задания пошагово: написали строку -> проверили, что она делает -> перешли к следующей.
# Для вывода значений используйте команду(функцию) print(). Можно перечислять сразу несколько значений.
# Для отделения целой части от дробно числа можно использовать команду(функцию) int()
# Основные арифметические действия: +, -, *, /, //, %, **.
# Основные операторы сравнения: <, >, ==, !=, <=, >=.
# Логические операторы: or(или), and(и).