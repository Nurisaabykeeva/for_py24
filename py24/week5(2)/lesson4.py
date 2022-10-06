#Декораторы в Python 


#Декоратор - это фукцимя которая в свою очередь принимает другую функцию.Декоратор позволяет обернуть другую функцию для расширения её функционала без изменения её кода


# from symbol import decorator


# def decorator_func(func):
#      def wrapper(some_data):
#          return f'Вы передали: {func (some_data)}'
#      return wrapper
# @decorator_func(func):
# def get_name(name):
#      return name

# def get_last_name (last_name):
#     return last_name
# def get_age(age):
#      return(age)
# print(get_name('John'))
# print(get_last_name('Snow'))
# print(get_age(22))

# print(decorator_func(get_name('John')))




# # def decorator_func(func):
# #     print('Hello John')
# #     return func()

# # def func():
# #     print('hello2')
# #     return 'Hey'
    
# # res = decorator_func(func)
# # print(res)


# def to_upper_dec(func):
#     def wrapper():
# #res = func()
#     #  return 'fffffff'
# #     return wrapper

# # @ to_upper_dec
# # def get_name():
# #     return 'John'

# # @ to_upper_dec
# # def get_last_name():
# #     return 'Snow'
# # print(get_name())

# def func_dec(f):
#     def wrapper():
#         print('Я код который отрабатывает до вызова func1')
#         f()
#         print('Я код который сработает после!')
#     return wrapper

# @func_dec
# def func1():
#     print('Я функция func1')
# func1()


# def decorator(func):
#     def wrapper():
#         print('ПРивет')
#         func(*args, **kwargs)
#     print('Пока')
#     return wrapper

# @decorator
# def func_without_params(name, last_name):
#     print('Func without params')

# @decorator
# def func_with_params(name, last_name):
#     print('Func without params')
#     print(name, last_name)

#     func_without_params()
#     func_with_params('John', 'Snow')


# def deiv_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(func,_name_)
#         return wrapper
        

# @div_decorator
# def_get_info(name, last_name):
#     return name, last_name + 'Hello'

# print(get_info('John', 'Snow'))

   
def dec_(func):
    def wrapper(l):
        res = 


def get_sum(list_):
    res = 0
    for i in list_:
        res += i
        return res

get_sum([1, 2, 3])
    