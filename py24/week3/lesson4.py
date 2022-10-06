#кортеж,цикл for,range


#tuple -> Кортеж (неизменяемый,упорядоченный,итерируемый)

# from sre_constants import _NamedIntConstant


# names = ('John', 'Sam', 'Tolik')
# print(type(names))
# print(names[0])
# print(dir(names))
# count_name = names.count('John')
# print(count_name)
# print(names.index('Sam'))

# for i in names
# print(i)


######
#цикл используется в тех случаях,когда  нужно повторить что-нибудь n-ое количество раз или прройтись по итерируемому объекту

# for i in range(0, 11, 2):
#     print(i) #0, 2, 4, 6

# for i in range(5,11): #от 5 до 10
#     print(i)

# l = range(10)
# print(list(l))
# l = range(5)
# for i in l:
#     print(i)



# list_ = range(0, 21)
# for i in list_:
#     if i % 2 == 0:
#         print(f'{i} - чётное')
#     else:
#         print(f'{i} - нечётное')  


# list_ = range['Alex', 'John', 'Sam', 'Rachel', 'Tolik']
# for i in list_:
#     if






# list_ = range(0 , 21)
# l1 = []
# l2 = []
# for i in list_:
#     if i % 2 == 0:
#      l1.append(i)
#      print



#break, continue, pass


# if True:
#     pass
# for i in range(10):
#     pass


# for i in range(10):
#     print(i)
#     break
#     if i == 5:
#         break # досрочно останавливает цикл


# for i in range(10):

#     if i ==5:
#         continue # продолжает цикл после остановки,пропусти все что находится ниже и приступи к следубщей итерации
#     print(i)

# for i in range(5):
#     print(i)
# else: #работает только тогда когла вышли из цикла без помощи break
#     print('END')


# list_ = range['Alex', 'John', 'Sam', 'Rachel', 'Tolik']
# for i in list_:
#     if i == 'John':
#         continue
#     print(f'Привет{i} пойдём тусить без John')

list_ = [['John', 22], ['Sam' 11], ['Tolik', 45]]
for i in list_:
    if i [1] >= 18:
         print(f'Привет {i[0]} тебе {i[0]} лет,ты проходишь')
    else:
        print(f'Привет {i[0]} через {18 - i[1]} лет приходи')
















# test = 'hello'
# for i in test:
#     print(i)

# text = 'The littli brown fox jumps over the lazy dog'
# result = text.replace('o', '*')
# print(result) # 

# result2 = ''
# for ch in text:
#     if ch == 'o':
#         result2 = result2 + '*'
#     else:
#         result2+=ch
# print(result2)


# text = 'The littli brown fox jumps over the lazy dog'
# result1 = text.lower().count ('t')
# print(result1) # 4

# result2 = 0
# for ch in text.lower():
#     if ch =='t':
#         result2 += 1
# print(result2)

text = 'The littli brown fox jumps over the lazy dog'
result1 = text.isupper()
# print(result1)

small_letters = []
big_letters = []
for i in range(65, 91): # или for i in range(ord('A'), ord('Z'))
    big_letters.append(i)
print(big_letters)
print(ord('A'), ord('Z'))




