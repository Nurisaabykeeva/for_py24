#lambda - это анонимная функция которая имеет более краткую запись и чаще всего вызывается только один раз

#lambda arguments:expression - синтаксис

# def get_sum(a,b):
#     return a + b

#a = get_sum(2,3)
#print(a)


# a = lambda a, b: a + b
# print(a(5, 5))


# a = lambda y, z: y + z
# print(a(3, 5))

# a = lambda x, y, z:(x + y )* z
# print(a(2, 3, 4))




# #split and join
# s = 'hello john snow'
# l = s.split('l')
# print(l)

# l = ['hello', 'john', 'snow']
# s = ''.join(l)
# print(s)

# l = ['a', 'aa', 'b', 'fff']
#l.sort(reverse=True)
# l.sort(key=len)
# print(l)


# s = 'sadsghjnk'
# s2 = sorted(s)
# # print(s2)
# s3 = ''.join(s2)
# print(s3)

#Константа
# AGE = 18

import random
# l = ['John', 'Snow', 'Tolik']
# answer = random.choice(l)
# print(answer)
#print(dir(random))




# def f():
#     global x
#     x = 100
# f()
# print(x)


# x = 100
# def f():
#     x = 30
#     print(id(x))
# print(id(x))
# f()




# x = 10
# def f1():
#     global x
#     x = 20
#     print(x)
#     def f2():
#         nonlocal x
#         x = 30
#         print(x)
#     f2()
# print(x)
# f1()


#help()

# #import time
# import time
# import datetime
# print(datetime.datetime.now())
# for i in range(10):
    # print(i)
    # time.sleep(1)

    #55 -> 10

def sum_dugits(num):
    for i in num:
        print(i)
        print(sum_dugits(num)):
        r += i
    return 













