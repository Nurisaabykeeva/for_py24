# CRUD магазина на функциях
    # C - CREATE 
    # R - READ
    # U - UPDATE
    # D - DELETE
import datetime
  
data = [
    {
        'id': 1,
        'name': 'product1',
        'price': 100,
        'created_at': datetime.datetime(2022, 10, 4),
        'is_active': True
    }
]

def get_products():
    return data

def get_one_product(id): # 
    product = [i for i in data if id == i['id']]
    if product:
        return product[0]
    return 'Нет такого продукта!'


def post_product():
    max_id = max([i['id'] for i in data]) 
    new_data = {
        'id': max_id + 1,
        'name': input('Введите имя товара: '),
        'price': int(input('Введите цену: ')),
        'created_at': datetime.datetime.now(),
        'is_active': True
    }
    data.append(new_data)
    
    return f'Вы добавли новый товар:\n {new_data}'

def delete_product(id): # 1
    delete_product = [i for i in data if i['id'] == id] # [{'id':1}]
    if delete_product:
        # print(delete_product)
        data.remove(delete_product[0]) # [{}]
        return 'Успешно удален!'
    return 'Нет такого продукта!'


def update_product(id): # 2
    update_product = [i for i in data if i['id'] == id] # [{'id'}]
    
    if update_product:
        index_item = data.index(update_product[0]) # 
        
        if input('Хотите обновить имя?: ') == 'Да':
            data[index_item]['name'] = input('Введите новое имя: ')
        if input('Хотите обновить цену?: ') == 'Да':
            data[index_item]['price'] = int(input('Введите новую цену: ')) 
        return 'Удачно обновили!'   
    return 'Нет такого продукта!'

def main():
    while True:
        print('Привет вот функцонал: \n1 - получить все товары \n2 - получить определенный товар \n3 - создать товар \n4 - удалить товар \n5 - обновить товар')
        method = input('Введи число: ')
        if method == '1':
            print(get_products())
        elif method == '2':
            id = int(input('Введи id товара: '))
            print(get_one_product(id))
        elif method == '3':
            print(post_product())
        elif method == '4':
            id = int(input('Введите id товара который хотите удалить: '))
            print(delete_product(id))
        elif method == '5':
            id = int(input('Введите id товара который хотите обновить: '))
            print(update_product(id))
        else:
            print('Нет такого функционала!')
    
    

if name == 'main':
    main()

    



