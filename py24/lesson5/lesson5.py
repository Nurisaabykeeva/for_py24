# x = 2
#x = x + 3
#print(x)

# == vs is
# l = [1]
# l2 = [1]
# print(l == l2) #True
# print(id(l))
# print(id(l2))
# print(l is l2) #False




# list_ = ['a', 'b', 'c', 'd']
# # count_ = 0
# # for i in list_:
# #     print(f'Под индексом {count_}находится {i}')
# #     count_+=1

# for i in range(len(list_)): #range(4)
#     print(f'Под индексом {i} находится {list_[i]}')

# l = ['name', 'age']
# d = dict.fromkeys([1, 2, 3])
# print(d)

# d = {'age': 22}
# a = d.setdefault('age2')# если находит то вытаскивает ключ,если нет,то создаёт новый
# print(a)
# print(d)

# d = {
#     'John': {
#         'age': 22,
#         'last_name':'Snow',
#         'weight':'90'
#     }
# }
# print(d['John']['age']) #22

# print(dir(list))
# l.append

# for i in range(1, 11): таблица умножения от 1 до 10
#     for a in range(1, 11):
#         print(f'{i} * {a} = {i * a}')

# = vs ==
#PEP8

# d = {'a': 2, 'b': 4, 'c':5}
# d = {'k': 'Чётное' if v % 2 == 0 else 'Нечётное' for k, v in d,items()}
# #print(d)

# d = {'a': {'John': 2}, 'c': {'SAm': 25}}
# #d = {'a': 2, 'c': 25}
# d = {k: v for k, v in d.items()
# for k2, v2 in v.items()}
# print(d)

dict_ = {'Timur':{'history': 90,'math': 95, 'literature':91}}   







