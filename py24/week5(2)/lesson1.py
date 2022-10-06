#Введение в функцию.Позиционные и именованные,args,kwargs параметры по default


#Встроенные функции - len,print,sum,max,min,dir,int,list и т.д.


# def get_sum():
#     print('Hello John')
# get_sum()
# get_sum()

# def get_sum(x, y): #параметры
#     print(x)
#     print(y)

# get_sum(2,3) #аргументы

# def get_sum(x,y):
#     s = x + y 
#     return s е return функция перестаёт работать#посл
#     #print(len('f'))   #после return функция перестаёт работать
# print(get_sum(2,3))

# def get_result(x, y, z):
#     return x * y *z
# print(get_result(1, 2, 3))

#Аннотации фукций

# def func1(x, y):
#     return x + y

# print(func1(2,3))
# print(func1('Jo','hn'))


# def func2(x='Tolik'):
#     return x + 'Hello'
# print(func2('John'))
# print(func2())

# def func3(x, y, z=2):
#     return x+z+y
# print(func3(3, 6))

# list_ = [1, 4, 6, 2]
# s = 0
# for i in list_:
#     s += i
# print(s)

# list_ = [1, 4, 5, 7]
# def my_sum(l):
#  s = 0
# for i in l:
#     s += i  неправильно!!!!
# print(s)


# def func4(x, y, z):
#     print(x, y, z)
# #     pass
# # func4(2, 3, 5) #передали как позиционные аргументы
# # func4(y=5, z=2,x=3) #передали аргументы как именнованные
# #func4(x=5, 4, 3) #Error после именнованных аргументов не могут идти позиционные аргументы
# func4(5, z=2, y=4)

# *args и **kwargs - позиционные и именнованные аргументы

# def func5(x, y, z, d):
#     return x + y +z + d
#     func5(5, 4, 2, 1)

# def func5(x,y, *args, **kwargs):
#     print(args) #tuple
#     print(kwargs) #dict
#     return x + y + sum(args)
# print(func5(5, 4, 6, c=7))


#1,4 -> 1,2,3,4
# def func5(x, y):
#     res = list(range(x, y+1))
#     print(res)
#     return res
# print (func5(1,4))


# def f():
#     if False:
#         return 'f'
#     else:
#         return 't'
#     print(f())

# def func7(x, y):
#     print(x + y)
#     return 'JOHN'

# func7(2,3)
# print(func7(2,3))


def func8(l, *args):
    print(l, args)

func8([1,23], 'john','tolik')
print(func8(1, 23))