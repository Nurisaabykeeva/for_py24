#import this


#Функция высшего порядка - это функция которая может принимать в качестве аргумента другую функцию
 #и (или) возвращать как результат работы


# l = [(1, 2, 3),('hello', 'john', 'snow')]
# for i, i2, i3 in l:
#     print(i, i2, i3 in l)

# l= ['a', 'b', 'c', 'd']
# for i, j in enumerate(l):
#     print(i, j)

# def map_(func,iter_object):
#     new_list = []
#     for i in iter_object:
#         new_list.append(func(i))
#     return new_list
# l = [1, 2, 3]#
# print(map_(lambda x: str(x), l))

# def filter_(func, iter_obj):
#     new_list = []
#     for i in iter_obj:
#         if func(i):
#             new_list.append(i)
#     return new_list
# l = [1, 2, 3, 4]
# print(filter_(lambda x: x % 2 == 0, l))