# [
#     {
#         "id": 1,
#         "name": "Ball",
#         "price": 100.0
#     }
# ]
import json
FILE_PATH  = 'data.json'
def get_data():
    with open(FILE_PATH) as file:
        data = json.load(file)
    return data
    
def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data
    return 'No such data'
def post_data():
    data = get_data()
    maxid = max([i['id'] for i in data ])
    data.append({
        'id': maxid+ 1,
        'name': input('enter the name: '),
        'price': float(input('enter the price: '))
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        return 'created'
def update_data(id):
    data = get_data()
    data_update = [i for i in data if i['id'] == id] 
    if data_update:
        index_ =  data.index(data_update[0])
        data[index_]['name'] = input('Введи новое имя! ')
        data[index_]['price'] = float(input('Введите новую цену: '))
        json.dump(data,open(FILE_PATH, 'w'))
        return 'UPDATE!'
    return 'Нет такого товара!'
def delete_data(id):
    data = get_data()
    data_delete  = [i for i in data if i['id'] == id]
    if data_delete:
        data.remove(data_delete[0])
        json.dump(data, open(FILE_PATH,'w'))
        return 'DELETED'
    return 'Нет такого товара'



