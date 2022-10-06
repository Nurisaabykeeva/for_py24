# for i in range(3):
#     for j in range(i):
#         print(j)


        #множество в Python
        # Set(множество)это изменяемый,неупорядоченный и итерируемый тип данных,который хранит в себе только уникальные значения,а также хранит в себе только неизменяемый тип данных
        

    #{} - у set такой литерал

    # s = {}
    # print(type(s)) # dict
    # s = set
    # print(type(s)) #set

    # s = {1, 1, 1, 1, 1, 1, 'hello', 'hello'}
    # print(s)
    # s = 'abcabcabc'
    # l = list(s)
    # set_ = set(s)
    # print(l)
    # print(set_)

# print(dir(set))
# a = {1, 2, 3}
# b = {3, 2}
# print(a.union(b))
# print(a.intersection(b))

#### copy vs deep copy
# import copy
# l1 = [1, 2, ['hello', 'g']]
# # l2 = l1
# l2 = l1.copy() #поверхностное копирование 
# l2 = copy.deepcopy(l1)
# l2[0] = 'hello'
# print(id(l2))
# print(id(l1))
# print(l1)
# print(l2)
# frozenset неизменяемое множество

# from itertools import count


# admin = {
#     'id': 1,
#     'name': 'John',
#     'password': 'Snow'


# }
# count_ = 3

# while input() != admin['password']:
#     count_-=1
#     if count_ == 0:
#         print('НЕ ЗАЙДЁШЬ!')
#         break
# else:
#     print('Hello')


for i in range(1,101):















