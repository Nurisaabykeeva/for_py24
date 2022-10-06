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

# # small_letters = []
# # big_letters = []
# # for i in range(65, 91): # или for i in range(ord('A'), ord('Z'))
# #     big_letters.append(i)

text = 'The littli brown fox jumps over the lazy dog'
result1 = text.isupper()
# print(result1)

small_letters = []
big_letters = []
for i in range(65, 91): # или for i in range(ord('A'), ord('Z'))
    big_letters.append(i)
result =None

for ch in text:
    if ord(ch) not in big_letters:
        result = False
        break
    else:
        result = True


print(result, text.isupper())