# def func1(num1: int, num2: int=2 *args: int, **kwargs):
#     print(num1)
#     print(num2)
#     print(args)
#     print(kwargs)

#     func1(1, 2, 3, 4, k=2)


def validate_email(email):
    if not '@' in email:
        raise Exception ('Введите символ - @')
        elif len(email) < 10:
            raise exception('Слишком короткий email')
    pass

#list_ = ['admin@admin.com', '1@1.com', '23@gmail.com']
email = 'admin@admin.com'
print(validate_email(email))
