# Первое задание. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):

    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res

print(f'result  {div()}')

# Второе задание. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input('Ваше имя :')
surname = input('Ваша фамилия :')
year = int(input('Ваш год рождения :'))
city = input('Город :')
email = input('Email :')
telephone = input('Telephone :')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Cherepenin', name = 'Andrey', year = '1985', city = 'Msk', email = '1@mail.ru', telephone = '123456789'))

# Третье задание. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первый аргумент : ")), int(input("Введите второй аргумент : ")), int(input("Введите третий аргумент : ")))}')

# Четвертая задача. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#
def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(2, -3))

# Пятая задача. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

import sys

result = 0
while True:
    line = input("Enter number or special token q fo exite: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)
#print(result)
#exit()

#Шестая задача. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()

def func(a):
        return a.title()
print(func("abcd erty"))

print this
