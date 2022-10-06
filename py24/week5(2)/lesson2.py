#области видимости и пространство имён

#Аббревиатура:
#LEGB - Local, Enclosed,Global,Built-in

#Область видимости определяет как переменные и имена ищутся в вашем коде.Область видимости имени или переменной завсист от того места в коде,где вы создаёте переменную
#x - это глобальная переменная

# def func1():
#     x = 'Это замкнутая переменная'

#     def func2():
#         x = 'Это локальная переменная'

# print(x)


# x = 2
# def f():
#     y = 2
#     print(locals())
#     f()
# print(globals())


# x = 0
# def counter():
#     global x
#     x += 1
#     print(x)
# counter()
# counter()
# counter()

x = 10
def f():
    x = 20
    def f2():
        #nonlocal
        x = 40
    print(x)
    f2()
print(x)
f()