# Первая задача. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 22
b = 4
print("Переменные a и b - ", a, b)
string_1 = input("Введите год рождения:")
number_1 = int(input("Введите дату рождения:"))
string_2 = input("Введите год рождения дочери:")
number_2 = int(input("Введите дату рождения дочери:"))
print("Введеные значения - %10s %5d %10s %5d" % (string_1, number_1, string_2, number_2))