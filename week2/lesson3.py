# Типы данных: String(строка)

#Что такое строка?
# Строка в  Python - это последовательный набор символов,который  может состоять как из цифр,так и из букв и разделителей

# Строка это неизменяеммый упорядоченный,индексируемый тип данных

# Конкатенация - сложение строк
# h = hello
 # w = world
 # print(h_w)
#  print('hello' +'2') #hello2
#  print('hello'+2)#Error
#  print('2' + 2)#22
#  print('2' + 2)#error

#text = 'hhaxjhv,jzVvaxsgvjhzG..//...//.'
#print(len(text))
#   Интерполяция строк (форматирование строк) (эф строки)


# print('hello "world"')
# print("hello 'world'")
# print("I'am")
# print('hello 'hello'')
# print("hello "hello"")


#Срезы (slice)
# s = 'hello'
# # 01234
# print(s)
# print(s[0])
# print(s[2])

# h = 'hello world'
# print(h[-1]) #d
# print(h[-3]) #r


# h = 'hello'
# print(h[0:2]) #he
# print(h[2:-1]) #ll
# print(h[:2]) #he
# print(h[3:]) #lo
# print(h[:]) # hello

# h = 'hello'
# print(h[0:4:2]) #hl
#print(h[::-1]) olleh


# text = 'spam'
# print(text[2])
# print(text[-2])
# print(text[2:4])#am
# print(text[2:])#am
# print(text[1:3])#pa
# print(text[::2]) #sa
# print(text[::-1]) #maps


#Экранированные последовательности - это последовательности которые нвчинаются с символа \ за которым следует один или более символов
#print('hello\nworld') #переход на следующую строку


# print('hello\tworld')    #табуляция это четыре пробела 

# print('I\'am') #\' игнорировать
# print(r'\n) переводит на следующую строку') r отменяет экранированную последовательность




#lesson4


#print(dir(str))

# text = 'hello world'
# print(text.isdigit()) #состоит ли строка только из цифр
# print('john' .isdigit())#false
# print('john22' .isdigit())#false
# print('2143124312' .isdigit()) #True


# print('john22'.isalpha()) #Состоит ли строка из букв
# print('john'.isalpha())


# print('f 8'.isalnum()) #состоит ли строка только из цифр и букв #false
# print('f8'.isalnum())

# print('john'.islower()) #состоит ли строка из букв в нижнем регистре(с маленькой буквы)
# print('john'.isupper()) #в верхнеи регистре
# print('john'.istitle()) #начинаются ли слова с большой буквы
# print('john'.isspace())# состоит ли строка из символов(пробел,\n,\t и тд)

# s =  'Sam'
# print(s.upper()) #SAM

# print('john'.upper()) #переводит в верхний регистр
# print('john'.lower())#переводит в нижний регистр
# print('john'.title())#меняет первую букву каждого слова в верхний регистр,а остальные буквы в нижний регистр
# print('john WORLD'.swapcase())#переводит всё наоборот (Wh -> wH)
# print('john hello'.capitalize())#переводит первый символстроки в верхний регистра все остальные в нижний
#name = "john"
# name = name.title()
#print(name) #John

# text = 'hello,world,he,she,it,i'
# print(text.split(',')) #Разбиение строк по разделителю
#['hello', 'world', 'he', 'she', 'it', 'i']

# s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaawwwwwwwwwwwww'
# print(s.count('a'))
# print(s.count('w'))
# print(s.count('aw'))

# print('hello hello hel'.count('hel'))
# print('hello hello hel'.count('hello'))
#print(s.lstrip())#удаляет слева все пробелы
#print(s.rstrip())#удаляет все пробелы справа
#print(s.strip())#удаляет и слева и справа

#print('hello.......'.rstrip(','))
