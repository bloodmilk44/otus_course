import json
from csv import DictReader


with open('../files/books.csv', newline='') as b:
    reader = DictReader(b)

    title_list = []
    author_list = []
    height_list = []

    for row in reader:
        title = str(row['Title'])
        author = str(row['Author'])
        height = str(row['Height'])

        #  Получаем списки всех книг, авторов и количества страниц
        title_list.append(title)
        author_list.append(author)
        height_list.append(height)


with open("../files/users.json", "r") as f:
    data_list = json.loads(f.read())

for name in data_list:
    name_user = name['name']
    gender_user = name['gender']
    address_user = name['address']

    #  Генерируем структуру для генерации JSON
    result = json.dumps({'name': name_user, 'gender': gender_user, 'address': address_user,
                         'books': [{'Title' : title_list.pop(),
                                    'Author' : author_list.pop(),
                                    'Height' : height_list.pop()}]}, indent=4)

    with open("../files/example.json", "w") as g:
        for row in result:
            print(result)
            g.write(result)



