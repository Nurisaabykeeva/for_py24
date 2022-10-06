#Файлы.Модули.Import(from).
#Работа с файлами (чтение и запись)


#Модуль это файл .py,который содержит некоторые функции и переменные.При необходимости они могут быть импортированны.
#(math, this, random, time)
#import math
#print(math.pi)
# pi = 'dasdasdasd'
# from math import pi as pi2
# print(pi)
# print(pi2)


#from math import * #импортировать всё










#print(pi)

#Пакет состоит из модулей,используется для того чтобы упаковывать файлы для удобства хранения и управления.Первым файлом в пакете является __init__.py


#Библиотека - это просто набор модулей,пакетов,функций и тд



# from helper import age,get_name
# print(age)
# print(get_name('John'))

# if __name__ == '__main__':

###файлы

#ПРи помощи питона можно работать с файлами (создавать,добавлять,считывать,изменять)


#open() - встроенная функция позволяющая открыть какой-либо файл


# file = open('test.txt', 'r')
# print(file.tell())#говорит где находится курсор
# print(file.read())#Считывает всё содержимое
# print(file.tell())
# print('*******')
# print(file.read())
# print('*****')
# file.seek(18)
# print(file.read())
# file.close()

# f = open('test.txt')# по умолчанию режим 'r'(read)

# data = f.read(8)
# print(data)
# print(f.read())
# print(data)
# f.close()

# print(f.readline())#считывает одну строку
# f.close()


# print(f.readlines())#возвращает список со всеми элементами

# f = open('test.txt')
# for i in f:
#     print(i)


#Запись в файл
#'w' - открывает на запись,содержимое файла удаляется,если файла не существовало то создаётся новый


# file = open('test2.txt', 'w')
# file.write('hello')
#file.write(18)ERROR
# file.write(str(18)
# file.write(['a', 'b'])#ERROR
# file.writelines(['a\n', '\tb'])#ожидает коллекцию
# file.close()

# with open('test.txt') as file:
#     print(file.read())
# print(file.read())

# with open('test3.txt', 'a') as file:
#     file.write('HELLO')

# with open('test.txt', 'r') as file:
#     print(file.read())
#     with open('test.txt', 'a') as file2:
#         file2.write('\nSnow')


# with open('test.txt', 'r+') as file:
#     print(file.read())
#     file.write ('fffffff')


# with open('task.txt') as f1:
#  res = f1.readlines()
#  res = [int(i.replce('\n','') for i in res]
#     with open('result.txt', 'w')
#     as f2:
#     f2.write(f'{max(res)}-{min(res)}')

#5678910
# with open('result.txt', 'w') as file:
#     for i in range(5,11):
#         file.write('\t'str(i)+'\n')

# with open('result3.txt', 'x') as file:
#     file.write('sadads')

#JSON(Javascript jbject notation)- простой формат обмена даннымию.Людям легко ег читать и вести в нём записи,а компьтеры запросто с его синтаксисомю
#В основном его применяют для пересдачимежду сервером и веб-приложением(обмен между фронтом)

import json
data = {'name': 'John', 'age': 22, 'name2': None, 'is_admin': True}
json_obj = json.dumps(data) #перевели данные в json(Сериализация) когда наоборот с json в питон (дисериализация)
print(json_obj)
python_obj = json.loads(json_obj) #перевели  json в питон десериализация)

# Разница типов данных

# Python  JSON
# dict      Object
# list      Array
# tuple      Array
# str      String
# int      Number
# float      Number
# True      true
# False      false
# None      null

with open('data.json', 'r') as file:
    # python_data = json.loads(file.read())
    # print(python_data)

    # python_data  = json.load(file) #load dumps работает с файлами
    # print(python_data) 

    #разница между методами load() b loads() а так-же между dump() и dumps(), в том что load и dump принимает весь файл и автоматически вериализует


    import json
    with open('data.json', 'w') as file:
        json.dump([True, False], file)