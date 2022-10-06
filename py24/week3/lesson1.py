# print(bool(1)) #True
# print(bool(0)) #False
# print(bool(200)) #True
# print(bool(0.1))#True
 #boolean - неизменяемый тип данных

 #nontype - это  ничего(нейтральное значение)

 # Лекция: Логические выражения и операторы Python (if). Nonetype. Условные операторы

# boolean - неизменяемый тип данных 

# True - Истина (да) (1)
# False - Ложь (нет) (0)



#s = 'hello'
#print('e in s') # True


#print(5 > 5 > 2 < 1) #False

#print(True == False and True == True) чтобы вышло true нужно чтобы с обоих сторон и слева и справ truedi
#print(True == True and True == True and False == True)

#Print(True or False) #True
#Print(5 > 2 or 5 > 6) #True

#print(True == True and False == False or 5 > 2) # True
#print (not True) #False
#print (not False) #True
#print(not False == True and (not True) == (not False))


# Условные операторы (if)
 

#  a = 2
#  b = 3
#  if a > b:
#     print('a больше')


# num = int(input('Введите число от 1 до 5'))
# if num > 5 or num < 1:
#     print('JOHN SNOW')
#     else:
#     print(f'Это {num}')




# age = int(input(' Введите свой возраст:'))
# name = input('Как тебя зовут?')
# if age >= 18 and name == 'John':
#     print('Привет,поздравляю ты новый админ!')
# elif age >= 18
#     print(f'добро пожаловать!')
# else:
#     print(f'ты слишком молод {name}!')
# print(f'Пока {name}!')

#тернарный оператор
# age = 18 
# if age == 18:
#     name = 'John'
# else:
#     name = 'Sam'
# print(name)

# 
# num1 = 5
# num2 = 6
# print('num1 > ') if num1 > num2 else print('num2 > ')


# print(max(1, 6, 3, 4))
# print(min(0, -1, 2, 4))
# print(sum([1, 2, 3]))

#ord
#chr
#print(ord('a'))
# print('abc' > 'h')
# print('abc' > 'aa')
# print(ord('a'))
# print(ord('h'))

# print(chr(97)) #a
# print(chr(1))


# lol -> lol
# hello -> olleh поллиндром

# num = 7
# if num % 2 == 0:
#     print('чётно!')
# else:
#     print('нечётное')



#list.py
#создание листов
# list_ = [] #литералы
# list_ = [1, True, [1, 2, 3], 'hello']
# list_[-1] = 'Makers'
# print(list)
# lst = [1, 2, 3, 4, 5]
# lst2 = [1, 2, 3, 4, 5]
# print(lst == lst2)

# list()
# a = list([1, 2, True])
# print(type(a))


#методы списков

#append(elemet) -> добавляет элементы в список(в конец списка)
# list_ = []
# inp = input('Tnter value: ')
# list_.append(inp)
# print[(list_)]

#range(start, end, step)

# ls = list(range(10))
# print(ls)

# list_ = [1, 3, True, 9, False]
# #print(list_[0])

# for elemet in list_: 
#     print(elemet)

# ls = []
# for i in range(11):
#     ls.append(i)
#     print(i)
# print(ls)

#extend(list) ->расширяет список добавляя в конец все элементы указанного списка
# ls1 = [1, 'hello']
# ls2 = [2, 'world']
# #ls1.extend(['makers',3, 5])
# print(ls1 + ls2) для объединения списков
# #print(ls2)

#insert(index, element) добавляет элемент в указанный индекс
# ls = [1, 3, 4, 5]
# ls.insert(1, '2')
# print(ls)

#remove(alement) Удаляет элемент списка (только первый попавший) ValueERror,если такого элемента нет

# l = ['h', 2, 'e', 8, 't', 'j', 'p', 10, 7]
# l.remove('h')
# print(l)

# #генерация списка из другого списка по условию
# ls = []
# for i in l:
#     if type(i) == int:
#         ls.append(i)
# print(ls)

#pop([i]) -> удаление i-го  элементаюВозвращает удалённый элементюУсли индекс не указан,удаляет последний элемент списка

# lst = [1, 'go', 'let', 4, True]

# print(lst.pop())
# print(a) #хранится удалённый элемент 'let'
# print(lst)


#index(element, [start,end]) возвращает положение (индекс) элемента (в указанном диапазоне)

# ls = [1, 5, 73, 7, 47,100, 8, 0, 9, 0, 1]
# print (ls.index(100, 3, 8))

# count(element) -> возвращает количество элементов в списке
# ls = ['h', 'e', 'l', 'l', 'o']
# print(ls.count('l'))

# sort(reserv = true, key=функция) -> сортирует список на основе функции
# ls = [5, 6, 2, 1, 7, 4, 3]
# ls.sort()
# print(ls)

# ls = ['ffygh', 'aj', 'eiii', 'b', 'o']
# ls.sort(key=len) сортировка по длине элемента
# print(ls)

# ls.sort(reserve=False, key=len)#переворачивает отсортированный список
# print(ls)
# reverse(переворачивает список)
# ls = [3, 5, 2, 6, 7]
# ls.reverse()
# print(ls)

# split(разделитель) -> преобразовывает строку в список по разделителю
# a = input('Введите слова через пробел: ')
# b = a.split()
# print(b)


#''.Join(list) используется для преобразования списка в строку
# ls = ['hello', 'world']
# ''.join(ls)
# print(a)

#copy()поверхностное копирование
# ls = [1, 3, 5, 7, [1,4,6,7]]
# ls2 = ls.copy()
# ls[-1].append(0)
# print(ls2, ls)

# leha = [100, 500, 1000]
# alexey = leha
# alexey.pop()
# print("A",alexey)
# print("L", leha)

# import copy
# ls = [1, 3, 5, [1, 3, 5, 7]]
# ls2 = copy.deepcopy(ls)
# print(ls2)

#clear() #Очищает список
# ls = [1, 'hello', 9, 10, 15]
# print(ls)
# ls.clear()
# print(ls)


