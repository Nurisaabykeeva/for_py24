#Лекция:обработка исключений.Оператор try except

#SyntaxError - забыли двоеточие,скобку и т.д.
#Ошибки - проблема в синтаксисе\
#indentationError - неправильный отступ


    #TabError - смешивание пробелов и табов

    ####исключения
# print('f') cработает
# 2 / 0 будет ошибка zerodevission error на ноль делить нельзя

#NameError (не было обнаружено имя)

#TypeError - когда тип объекта не подходит для определённой операции
#'2' + 2

#ValueError - когда тип объекта подходит для операции,но не его значение
# s = 'John'
# int(s)
#IndexError - обращение к несуществующему индексу
# l =[1]
# l =[100]

#KeyError - обращение к несуществующему ключу
# d = {1:1}
# d['John']

#ImportError - неправильный импорт 
#from math import pi2
#ModuleNotFoundError - не может найти такой модуль

#AttributeError - попытка вызвать несуществующий метод или атрибут у данного объекта
# x = 2
# x.isdigit()

#KeyboardInterrupt - исключение которое возникает когда пользователь нажимает определённые клавиши(например: ctrl + c)
# while True:
#     print('John')


# print('Hello world')
# x = int(input('Введите первое число: '))
# y = int(input('Введите второе число: '))
# print(x / y)

# print('Hello')
# a = 5 
# b = 'fdbvjdfbkjd'
# try:
#    print(a / b)
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#     #except NameError:
#      #print('НЕт такой переменной')
# except:
#     print('*******')


# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# try:
#   print(num1/num2)
# except:
#     print('На ноль делиить нельзя')


# try:
#     while True:
#         print('f')
#         except
#         print('Hello')


# try: #попытайся что-то сделать
#     pass
# except NameError: #сработает если в try случилась ошибка
#     else:#если ошибок не было
#         pass
#     finally: #в любом случае в конце сработает
#         #pass 


# try:
#     5 / 0
# except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# else:
#         print('Молодец!Не делил на ноль')
# finally:
#         
# print('Пока')

# name = 'John'
# if name == 'John':
#     raise ZeroDivisionError('ты John')
 
age = 10
try:
    if age < 18:

       raise ValueError('ты слишком молод!')
 except ValueError









