# list = [1, 2, 3, 4, 5]
# for i in list_:
#     print(i)

# while True:
#     print('Hey John')
# print('f')

# age = int(input('Введите ваш возраст: '))
# while age < 18:
#     age = int(input('Введите ваш возраст: '))
#     print('Ура ты прошёл!')
# list_ = [1, 2, 7, 8]
# i = 0
# while i < len(list_):
#     print(list_[i])
#     i += 1

# while True:
#     if int(input()) == 5:
#         break
# print('f')

###Тип данных - словари
# словарь - это изменяемый,упорядоченный и итерируемый тип данных
# {} - литералы
#синтаксиз - {'key': 'VALUE'}

# dict_ = {'key1': 'value', 'key2': 'value2'}
# print(len(dict_))



#ключи должны быть уникальными и неизменяемыми,а значения любые

# dict1 = {
#     'name': 'John',
#     'age': 22,
#     'hobby': [
#         'fishing',
#         'football'
#     ]
# }
# print(dict1['age'])  22
# print(dict1['hobby'][1]) football
# dict1['age'] = 21
# print(dict1)

# d = {
#     [1, 2, 3]: 'f'  #error
# }

# d = {
#     (1, 2, 3): 'f'
# }

# print(dir(dict)) 

# dict_ = {}

# dict_['name'] = 'f'
# dict_[1] = 'first'
# dict_[2] = 'first'
# dict_[2] = 'second'
# # print(id(dict_))
# print(dict_)


#методы словарей


# d = {1: 1}
# d.clear() #очищает
# print(d)
# #del d - удаляет переменную
# #print(d)

# list_ = [1, 2, 3]
# dict_ = dict.fromkeys(list_, 'number')
# print(dict_)

# d = {
#     'name': 'John'
# }
# # print(d['name2'])
# print(d.get('name2'))
# print(d.get('name2', 'John is not define'))

# d = {
#     'name': 'John',
#     'age': 22
# }
# # # remove_values = d.pop('age')
# # # print(d)

# # a = d.pop('age2', 'Нету!')
# # print(a)


# remoted = d.popitem()
# print(d)
# print(remoted)

# d = {
#     'name': 'John',
#      'age': 22
# }
# d2 = {
#     'age': 22,
#     'age' : 23
# }
# d.update(d2)
# d.update({'last_name': 'Snow'})
# print(d)
# age = d.setdefault('age') #возвращает значение ключа,но если его нет,не вызывает ошибку а создаёт новый ключ со значением None по умолчанию
# age2 = d.setdefault('age2')
# print(age)
# print(age2)
# d.setdefault('age3', 22)
# print(d)

print(dir(dict))
d = {
    'name': 'John',
    'world': 'hello',
    1:1
}
# #print(d)
# print(d.items())
# print(d.values())
# print(d.keys())

# for i in d:
#     print(i)
# for i in d.keys():
#     print(i)

# for i in d.values:
#     print(i)

for k, v in d.items():
    print(f'Это ключ - {k}, а это значение - {v}')

